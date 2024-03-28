from sqlalchemy import select

from notes.schemas import Note
from database import session_factory
from models import NoteOrm, UserOrm


class NotesRepository:

    @classmethod
    def get_all(cls, username: str):

        query = select(UserOrm).where(UserOrm.username == username)

        with session_factory() as session:
            result = session.execute(query)
            user = result.scalar_one()

            data = {note.id: note for note in user.notes}
            return data

    @classmethod
    def get_one(cls, username: str, note_id: int):
        query = select(UserOrm).where(UserOrm.username == username)

        with session_factory() as session:
            result = session.execute(query)
            user = result.scalar_one()

            for note in user.notes:
                if note.id == note_id:
                    return note

            return None

    @classmethod
    def create(cls, username: str, note_in: Note):
        data = note_in.model_dump()
        note = NoteOrm(**data)

        query = select(UserOrm).where(UserOrm.username == username)

        with session_factory() as session:
            result = session.execute(query)
            user = result.scalar_one()

            notes = user.notes
            notes.append(note)

            if user:
                user.notes = notes
                session.add(user)
                session.commit()



