## Internal Devops Utilities API

## AIM 

This project aims to deliver Production grade Utilities to Internal Teams 
- AWS Resources API
- System Metrics

## PRE-Requisite
- *Python* should be installed in the system
- AWS should be configured in the system using *aws configure*

## Usage

'git clone https://github.com/Yatingambhir85/DevOps-Utilities-API-Project.git '

## FOR LOCAL SERTUP

- Setup Python Virtual Environment

    python3.14 -m venv venv
    source venv/bin/activate

- Install Requirements

    pip install -r requirements.txt

- Run Application

    python3 main.py

- To access the application on browser

    http:127.0.0.1:8000

## FOR DOCKER SERTUP

- docker build -t utilities-project-image:latest .

- docker run -itd -v ~/.aws:/root/.aws:ro --name utilities-app -p 8000:8000 utilities-project-image:latest

## To access the application on browser

- http:127.0.0.1:8000

## To check the APIs and their usgae use the below URL

- http:127.0.0.1:8000/docs