from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from file_stream import FileStream
import json
app = FastAPI()

#origins = ["*"]
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/activities")
def get_activities():
    fs=FileStream()
    result = fs.get_file_stream("activity.json")
    return json.load(result)

