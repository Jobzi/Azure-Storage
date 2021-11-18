from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from file_stream import FileStream
import json
app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/activities")
def get_activities():
    fs=FileStream()
    result = fs.get_file_stream("activity.json")
    return json.load(result)

