# B"H
# script to start a FastAPI server

from fastapi import FastAPI
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware.cors import CORSMiddleware

#from pydantic import BaseModel
#from typing import List, Optional
#from bson.objectid import ObjectId
#from pydantic import parse_obj_as
#from datetime import datetime, timedelta

app = FastAPI()
origins = ["http://localhost:8000","http://localhost:5173"]
app.add_middleware(CORSMiddleware, allow_origins=origins)

@app.get("/")
async def root():
    return {"esg_api": "Running ok"}





