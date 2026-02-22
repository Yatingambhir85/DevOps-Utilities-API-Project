from app.api import app
import uvicorn
#python entry point for the application

if __name__=="__main__":
    #ASGI server to run the FastAPI application - Async Server Gateway Interface
    uvicorn.run("app.api:app", host="127.0.0.1", port=8000, reload=True)