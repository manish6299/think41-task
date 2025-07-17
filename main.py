from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from uuid import uuid4

app = FastAPI()

# Data storage
posts_db: Dict[str, dict] = {}

# Request model
class PostCreate(BaseModel):
    content: str
    author: str

# Response model
class Post(BaseModel):
    id: str
    content: str
    author: str
    likes: int

@app.post("/posts/", response_model=Post)
def create_post(post: PostCreate):
    post_id = str(uuid4())
    posts_db[post_id] = {
        "id": post_id,
        "content": post.content,
        "author": post.author,
        "likes": 0
    }
    return posts_db[post_id]

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    del posts_db[post_id]
    return {"message": "Post deleted successfully"}

@app.post("/posts/{post_id}/like", response_model=Post)
def like_post(post_id: str):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    posts_db[post_id]["likes"] += 1
    return posts_db[post_id]

@app.get("/posts/", response_model=list[Post])
def list_posts():
    return list(posts_db.values())
