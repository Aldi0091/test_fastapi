from pymongo import MongoClient
from fastapi import FastAPI, Query, status
from pydantic import BaseModel, constr
from typing import List, Dict
from datetime import date


DB = "hosting_base"
MSG_COLLECTION = "hosting_items"


class Templ(BaseModel):
    email: str
    phone: str
    date: str
    text: str



app = FastAPI()


@app.post("/post_message", status_code=status.HTTP_201_CREATED)
def post_message(message: Templ):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}


@app.get("/geturl", status_code=status.HTTP_201_CREATED)
def get_message(email: str = Query(..., regex="[^@]+@[^@]+\.[^@]+"), phone: str = Query(..., regex="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")):
    """Get form by fields."""
    mess = {
        "email": email,
        "phone": phone,
    }
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find_one(mess, {"_id": 0})
        response_msg_list = []
        if msg_list is not None:
            response_msg_list.append(msg_list)
            return response_msg_list            
    return {
        "email": type(email).__name__,
        "phone": type(phone).__name__
    }
            

        
