from sqlalchemy import select

from database import session_factory
from models import UserOrm
from auth.schemas import User


class UserRepository:
    @classmethod
    def get_user(cls, username: str) -> UserOrm | None:
        with session_factory() as session:
            query = select(UserOrm).where(UserOrm.username == username)

            result = session.execute(query)
            user = result.one_or_none()

            if user:
                return user[0]

            return None

    @classmethod
    def add_user(cls, user_in: User):
        data = user_in.model_dump()
        with session_factory() as session:
            user = UserOrm(**data)

            session.add(user)
            session.commit()
