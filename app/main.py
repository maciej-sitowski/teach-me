from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from app.routers import questions, auth, user

app = FastAPI()
app.include_router(questions.router)
app.include_router(auth.router)
app.include_router(user.router)

origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Question API"}

add_pagination(app)
