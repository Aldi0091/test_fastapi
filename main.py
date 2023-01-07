from fastapi import FastAPI, Query, status
import uvicorn
from connect import Connection

database = Connection().database

app = FastAPI()
   

@app.get("/geturl", status_code=status.HTTP_201_CREATED)
async def get_message(email: str = Query(..., regex="[^@]+@[^@]+\.[^@]+"), phone: str = Query(..., regex="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")):
    """Get form by fields."""
    mess = {
        "email": email,
        "phone": phone,
    }
    msg_list = await database.find_form(mess)
    response_msg_list = []
    if msg_list is not None:
        response_msg_list.append(msg_list)
        return response_msg_list            
    return {
        "email": type(email).__name__,
        "phone": type(phone).__name__
    }
            
if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8001)

        
