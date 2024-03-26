from fastapi import APIRouter, Depends

from notes.schemas import Note, NoteItem, NoteItems
from notes.repository import NotesRepository

from auth.utils import get_username_from_token
from src.models import UserOrm

NoteList = []


router = APIRouter(prefix='/notes')

@router.get('/')
async def read_notes(current_user: str = Depends(get_username_from_token)):
    return NotesRepository.get_all(current_user)

@router.get('/{note_id}')
async def read_note(note_id: int, current_user: str = Depends(get_username_from_token)):
    return NoteList[note_id]

@router.post('/')
async def create_note(note: Note, current_user: str = Depends(get_username_from_token)):

    NotesRepository.create(current_user, note)

    return { "message": "OK" }

@router.delete('/{note_id}')
async def delete_note(note_id: int, current_user: str = Depends(get_username_from_token)):
    NoteList.pop(note_id)
    return { "message": f"Note from id: {note_id} deleted"}

@router.put('/{note_id}')
async def update_note(note_id: int, note_data: NoteItem, current_user: str = Depends(get_username_from_token)):
    pass
