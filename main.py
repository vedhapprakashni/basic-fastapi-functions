import fastapi
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel



app=FastAPI() 

class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None
    
class UpdateItem(BaseModel):
    name:Optional [str]=None
    price:Optional[float]=None
    brand:Optional[str]=None

@app.get("/")
def home():
    return {"data":"testing"}

@app.get("/about")
def about():
    return {"data":"about page"}
inventory={

}
@app.get('/get-item/{item_id}')
def get_item(item_id:int=Path(description="The ID of the item you want to get",gt=0,lt=3)):
    if item_id in inventory:
        return inventory[item_id]
    return {"error": "Item not found"}

@app.get('/get-by-name')
def get_item(name:Optional[str]=None):
    for i in inventory:
        if inventory[i]['name']==name:
            return inventory[i]
    return {'data':'not found'}

@app.post('/create-item/{item_id}')
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        return {'Error':'Item ID already exists'}
    inventory[item_id]={'name':item.name,'brand':item.brand,'price':item.price}
    return inventory[item_id]

@app.put('/update-item/{item_id}')
def update_item(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        return {'Error':'Item ID does not exist'}
    
    if item.name!=None:
        inventory[item_id]['name']=item.name
    if item.price!=None:
        inventory[item_id]['price']=item.price
    if item.brand!=None:
        inventory[item_id]['brand']=item.brand
    
    return inventory[item_id]