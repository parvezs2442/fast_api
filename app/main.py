from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message":"Welcome to fastAPI"}

@app.get("/about")
def about():
    return {"message":"About Page"}

@app.get("/contact")
def about():
    return {"message":"Contact Page"}


#Path parameter
@app.get("/products/{id}")
def get_products(id:int):

    return {"productsID": id}

#quary parameter
@app.get("/products")
def products(category: str):
    return {
        "category":category
    }


#Pydantic

class User(BaseModel):
    name:str
    email:str
    password:int

class UserResponse(BaseModel):
    name:str
    email:str

@app.post("/register", response_model=UserResponse)
def register_user(user: User):
    return user








