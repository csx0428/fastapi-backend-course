from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def creat_item(item: Item):
    print(f"received item: {item}")
    return {"message": "Item received","Item": item}