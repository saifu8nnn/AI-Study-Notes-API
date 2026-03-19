from fastapi import FastAPI,HTTPException,Depends
from fastapi import status
from .models import Note
from .models import NoteModel
from .database import engine,get_db
from sqlalchemy.orm import Session
from .ai_services import generate_summary
NoteModel.metadata.create_all(bind=engine)

app=FastAPI()
@app.get("/")
def hello():
    return{"message":"hello guyz welcome to study notes api"}

#Add a note
@app.post("/notes",status_code=status.HTTP_201_CREATED)
def add_note(note:Note,db:Session=Depends(get_db)):
    new_note=NoteModel(**note.dict())# ** to convert dictionary into keyword arguments for the NoteModel class
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    summary=generate_summary(new_note.content)
    new_note.summary=summary
    db.commit()
    db.refresh(new_note)
    return new_note

#Fetch all notes
@app.get("/notes")
def get_all(db:Session=Depends(get_db)):
    result=db.query(NoteModel).all()
    return result

#Fetch a note
@app.get("/notes/{id}")
def get_post(id:int,db:Session=Depends(get_db)):
   note = db.query(NoteModel).filter(NoteModel.id==id).first()
   if not note:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"note not found")
   return note


#Delete a note
@app.delete("/notes/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db)):
    note=db.query(NoteModel).filter(NoteModel.id==id).first()
    if note==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with id {id} is not found")
    db.delete(note)
    db.commit()


#Update a note
@app.put("/notes/{id}")
def update_post(id:int,update_note:Note,db:Session=Depends(get_db)):
    note=db.query(NoteModel).filter(NoteModel.id==id).first()
    if note==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    db.query(NoteModel).filter(NoteModel.id==id).update(update_note.dict())
    db.commit()
    updated_note=db.query(NoteModel).filter(NoteModel.id==id).first()
    return updated_note