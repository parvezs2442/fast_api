from fastapi import FastAPI, HTTPException

app = FastAPI()


# @app.get("/")
# def root():
#     return {"message":"Welcome to fastAPI"}


#id parameter
@app.get("/products/{id}")
def get_products(id:int):

    return {"productsID": id}

#quary parameter
@app.get("/products")
def products(category: str):
    return {
        "category":category
    }


@app.get("/about")
def about():
    return {"message":"About Page"}

@app.get("/contact")
def about():
    return {"message":"Contact Page"}









