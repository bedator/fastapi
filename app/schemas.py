from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

# POST SCHEMA

# Define a Pydantic model (Schema) for the post data
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

# Define a Pydantic model for the user response
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models

# Define a Pydantic model for the response
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models

# Define a Pydantic model for the post response with votes
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True  # This allows Pydantic to work with SQLAlchemy models

# USER SCHEMA

class UserCreate(BaseModel):
    email: EmailStr
    password: str


# USER LOGIN SCHEMA

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# TOKEN SCHEMA
class Token(BaseModel):
    access_token: str
    token_type: str

# TOKEN DATA SCHEMA
class TokenData(BaseModel):
    id: Optional[int] = None

# VOTE SCHEMA
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # type: ignore # 1 for like, 0 for unlike

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models