"""This is for test insertion to MongoDB"""
import asyncio
from connect import Connection

database = Connection().database


message_list = [
        {
        "email": "albert_einstein@gmail.com",
        "phone": "+7 999 777 00 01",
        "date": "2000-07-11",
        "text": "Invented Relativity"
    },
    {
        "email": "franz_kafka@gmail.com",
        "phone": "+7 999 222 00 01",
        "date": "2022-02-15",
        "text": "Writer"
    },
    {
        "email": "ronaldo@gmail.com",
        "phone": "+7 999 111 00 01",
        "date": "2023-04-19",
        "text": "Football Champion"
    },

]

loop = asyncio.get_event_loop()
tasks = (database.insert(message) for message in message_list)
coro = asyncio.gather(*tasks)
loop.run_until_complete(coro)
loop.close()




