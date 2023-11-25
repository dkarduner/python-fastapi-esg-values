B"H
# Python FastAPI Example
Script to start a FastAPI server.

## Markets insiders
The API retrieve stock data from markets.businessinsider.com

## Usage 
/stocksName : retrieve a list with S&P500 companies names and stocks names.

/stockPrice/{stock}: retrieve last 30 days prices - one per day.

## Conda environment (recommended)
Install conda / update current version:
$ conda --version
$ conda update conda

Create new environment:
$ conda create --name {new_env} python=3.11

$ conda activate {new_env}

## Installing requirements.txt
$ pip install -r requirements.txt

## Running the FastAPI server
Starting a server with hot module files reload option.
$ uvicorn main:app --reload --port 8000
The server will be started in: http://127.0.0.1:8000

In case of deploying in a server, use:
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000

## Documentation
FastAPI automatically generates documentation in:
http://127.0.0.1:8000/docs 


