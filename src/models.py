from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase


class Model(DeclarativeBase): pass


class UserOrm(Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    notes = relationship("NoteOrm", back_populates="user")


class NoteOrm(Model):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    body = Column(String)
    datetime = Column(String)
    user = relationship("UserOrm", back_populates="notes")
