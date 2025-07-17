# 📱 Social Media Post API

A simple RESTful API built with **FastAPI** that allows users to create, delete, like, and view social media-style posts. Ideal for learning how APIs work and for building minimal backend prototypes.

---

## 🚀 Features

- ✅ Create a new post
- ❌ Delete a post by ID
- ❤️ Like a post by ID
- 📃 List all posts with like counts

---

## 🧠 Approach & Architecture

This project uses an **in-memory dictionary** (`posts_db`) to simulate a database. It’s intentionally kept simple for learning purposes or prototyping. Here’s a breakdown of how it works:

### ➤ Data Storage
- Posts are stored in a global dictionary `posts_db`, where each key is a unique `UUID` representing a post.
- Each post is a dictionary containing:
  - `id`: Unique ID
  - `content`: Post content
  - `author`: Post creator
  - `likes`: Like count (starts at 0)

### ➤ API Design

| Method | Endpoint                | Description                  |
|--------|--------------------------|------------------------------|
| POST   | `/posts/`               | Create a new post            |
| DELETE | `/posts/{post_id}`      | Delete a post by ID          |
| POST   | `/posts/{post_id}/like` | Increment like count         |
| GET    | `/posts/`               | Get list of all posts        |

### ➤ Data Validation
- FastAPI uses **Pydantic** models to validate request and response data.
- `PostCreate` handles incoming post creation requests.
- `Post` is the response model used for post-related operations.

### ➤ UUIDs
- Each post is assigned a UUID using Python’s built-in `uuid4()` to ensure uniqueness.

---

## 📦 Tech Stack

- **Python 3.9+**
- **FastAPI** – for building the API
- **Uvicorn** – for serving the app
- **Pydantic** – for data validation

---
