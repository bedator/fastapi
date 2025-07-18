from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    created_at: datetime

    class Config:
        from_attributes = True

fake_posts = [
    Post(id=1, title="Post 1", content="Content 1", created_at=datetime.now()),
    Post(id=2, title="Post 2", content="Content 2", created_at=datetime.now()),
]

@app.get("/posts", response_model=List[Post])
def get_posts():
    return fake_posts
