# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Backend",
    description="Backend API for Next.js application",
    version="1.0.0"
)

# Allow Next.js frontend domain
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI server is up and running!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}