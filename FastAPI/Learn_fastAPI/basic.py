from  fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message' : 'This is a Webpage'}

@app.get("/about")
def about():
    return {'massage' : 'My name is rahul'}