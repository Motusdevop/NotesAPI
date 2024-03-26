from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from notes.router import router as notes_router
from auth.router import router as auth_router

from database import create_tables, drop_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting')
    create_tables()
    print('Success create tables')
    yield
    print('Off and drop tables')
    drop_tables()

app = FastAPI(lifespan=lifespan)

app.include_router(notes_router)
app.include_router(auth_router)

@app.get('/')
def index() -> dict:
    return { "message": "hello!" }

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)