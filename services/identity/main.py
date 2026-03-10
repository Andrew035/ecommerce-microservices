from datetime import datetime, timedelta

from fastapi import FastAPI
from jose import jwt

app = FastAPI()

SECRET_KEY = "2673"
ALGORITHM = "HS256"


@app.post("/login")
async def logic(username: str):
    # In a real app, verify against a DB here
    access_token_expires = timedelta(minutes=30)
    expire = datetime.utcnow() + access_token_expires
    to_encode = {"exp": expire, "sub": username}

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
