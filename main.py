# B"H
# script to start a FastAPI server

import requests, json, urllib3
#, os, time 

import esg_data
from calculate_esg import calculate_esg

from fastapi import FastAPI
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware

urllib3.disable_warnings()

app = FastAPI()
origins = ["http://localhost:8000","http://localhost:5173"]

app.add_middleware(
    CORSMiddleware
    , allow_origins=origins
    , allow_credentials=True
    , allow_methods=["*"]
    , allow_headers=["*"]
    )

@app.get("/")
async def root():
    return {"esg_api": "Running ok"}

@app.get("/esg_index/{ricCode}")
async def get_esg_index(ricCode: str):
    
    url = "https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode="+ricCode

    r = requests.get(url, verify = False)
    print(r.text)
    return {'ricCode': ricCode} 


@app.get("/ricCodes")
async def get_ric_codes():
    return {"data": "all ricCodes"}

