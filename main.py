from fastapi import FastAPI

app = FastAPI()  

@app.get('/')
def home():
    return  {"Greetings": "Hello, John Doe"}