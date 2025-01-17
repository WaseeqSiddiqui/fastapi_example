from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models,schemas,utils
from .database import engine
from .routers import posts,users,auth,votes

models.Base.metadata.create_all(bind=engine)

app=FastAPI(title="Weblog",summary="This is my newly created weblog app using FASTAPI",
description="this application enables you to post your own blogs, view other people posts and like them if you want.")

origins=["https://www.google.com","https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Hello World"}



  
