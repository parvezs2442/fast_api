from fastapi import FastAPI, HTTPException

app = FastAPI()


# @app.get("/")
# def root():
#     return {"message":"Welcome to fastAPI"}

@app.get("/products/{id}")
def get_products(id:int):
    products = ["Apple", "Mango", "Banana"]
    return products[id] if products[id] else HTTPException(status_code=404, detail="No data present with given id")












