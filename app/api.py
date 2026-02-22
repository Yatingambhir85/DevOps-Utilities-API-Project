from fastapi import FastAPI #Importing FastAPI class from fastapi module
from routers import metrics #Importing the metrics router from the routers package
from routers import aws #Importing the aws router from the routers package
#Creating an instance of FastAPI class
app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    docs_url="/docs",
    maintainer={
        "name": "Yatin Gambhir",
        "email": "yatingambhir85@gmail.com"},
    redoc_url="/redoc"
) 

@app.get("/")
def hello_world():
    """A simple endpoint that returns a greeting message."""
    return {"message": "Hello Dosto!! Welcome to FastAPI."}

app.include_router(metrics.router) #Including the metrics router in the main application

app.include_router(aws.router, prefix="/aws") #Including the aws router in the main application


