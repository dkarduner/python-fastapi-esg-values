B"H
# Python FastAPI
Script to start a FastAPI server.

# ESG index: Environmental, Social, and Governance index
The API retrieve data from Environmental, Social, and Governance index (the 'ESG index').
It uses the "ricCode" to extract data from:
https://www.refinitiv.com/bin/esg/esgsearchresult

# Conda environment (recommended)
Install conda / update current version:
$ conda --version
$ conda update conda

Create new environment:
$ conda create --name {new_env} python=3.11

$ conda activate {new_env}

# Installing requirements.txt
$ pip install -r requirements.txt

# Running the FastAPI server
Starting a server with hot module files reload option.
$ uvicorn main:app --reload --port 8000
The server will be started in: http://127.0.0.1:8000

In case of deploying in a server, use:
$ uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Documentation
FastAPI automatically generates documentation in:
http://127.0.0.1:8000/docs 


