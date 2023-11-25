# B"H
# script to start a FastAPI server

import stocks_data, markets_insider

from fastapi import FastAPI
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware

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
    return {"api": "running ok"}


@app.get("/stocksNames")
async def get_stocks_names():
    stocks = stocks_data.get()
    return {"data": stocks}


@app.get("/stockPrice/{stock}")
async def get_stock_prices(stock: str):
    prices = markets_insider.get_prices(stock) 
    return {'values': prices} 
