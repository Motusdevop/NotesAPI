from fastapi import APIRouter, Depends, HTTPException

from notes.schemas import Note, NoteItem, NoteItems
from notes.repository import NotesRepository

from auth.utils import get_username_from_token
from src.models import UserOrm

NoteList = []


router = APIRouter(prefix='/notes')

@router.get('/')
async def read_notes(username: str = Depends(get_username_from_token)):
    return NotesRepository.get_all(username)

@router.get('/{note_id}')
async def read_note(note_id: int, username: str = Depends(get_username_from_token)):

    note = NotesRepository.get_one(username, note_id)

    if note:
        return note

    raise HTTPException(status_code=404)

@router.post('/')
async def create_note(note: Note, username: str = Depends(get_username_from_token)):

    NotesRepository.create(username, note)

    return { "message": "OK" }

@router.delete('/{note_id}')
async def delete_note(note_id: int, username: str = Depends(get_username_from_token)):
    NoteList.pop(note_id)
    return { "message": f"Note from id: {note_id} deleted"}

@router.put('/{note_id}')
async def update_note(note_id: int, note_data: NoteItem, username: str = Depends(get_username_from_token)):
    pass
