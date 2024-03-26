from pydantic import BaseModel
from typing import List

class Note(BaseModel):
    title: str
    body: str
    datetime: str

class NoteItem(Note):
    id: int

class NoteItems(BaseModel):
    notes: List[NoteItem]