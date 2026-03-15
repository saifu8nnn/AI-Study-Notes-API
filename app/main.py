from fastapi import FastAPI,HTTPException
from fastapi import status
from app.models import Note
from random import randrange
app=FastAPI()
# List for storing notes
notes=[]
@app.get("/")
def hello():
    return{"message":"hello guyz welcome to study notes api"}

#finding post 
def find_post(id):
    for i in notes:
        if i["id"]==id:
            return i
#finding index
def find_index(id):
    for i,p in enumerate(notes):
        if p["id"]==id:
            return i

#Add a note
@app.post("/notes",status_code=status.HTTP_201_CREATED)
def add_note(note:Note):
    note_dict=note.dict()
    note_dict["id"]=randrange(1,10000000)
    notes.append(note_dict)
    return note_dict

#Fetch all notes
@app.get("/notes")
def get_all():
    return notes

#Fetch a note
@app.get("/notes/{id}")
def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with {id} is not found")
    return {"found post":post}

#Delete a note
@app.delete("/notes/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the post with {id} is not found")
    notes.pop(index)

#Update a note
@app.put("/notes/{id}")
def update_post(id:int,note:Note):
    post=find_post(id)
    index=find_index(id)
    note_dict=note.dict()
    note_dict["id"]=id
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    notes[index]=note_dict
    return note_dict

