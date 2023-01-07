import os
from mongo_client import get_DB

class Connection:

    def __init__(self):
        self.collec = os.getenv("MONGO_COLL", "hosting_items")
        self.database = get_DB(self.collec)