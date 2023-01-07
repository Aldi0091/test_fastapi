"""Project main database management module."""
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorDatabase
import conf.config as config



class MongoClient:
    """An object for establishing connection with a database on a mongodb-server.

    Its instance shall be shared between DB-instances.
    """

    def __init__(self, uri: str, db: str):
        self._client: AsyncIOMotorClient = AsyncIOMotorClient(uri)
        self.db: AsyncIOMotorDatabase = self._client[db]

    # def __del__(self) -> None:
    #     self._client.close()


class DB:
    """Database management client connected to a certain collection within one database.

    Awaits a {db}-attribute of a MongoClient-instance and a collection name.
    """

    def __init__(self, db: AsyncIOMotorDatabase, collection_name_1: str):
        self.collection: AsyncIOMotorCollection = db[collection_name_1]

    async def insert(self, message: dict) -> list:
        """The method to fetch the /id request and return list of jsons"""
        result = await self.collection.insert_one(message)
        print(result.inserted_id)

    async def find_form(self, message: dict) -> dict:
        result = await self.collection.find_one(message, {"_id": 0})
        return result
    

def get_mongo_client() -> MongoClient:
    """Get MongoClient instance."""
    return MongoClient(uri=config.mongo.uri, db=config.mongo.db)


def get_DB(collection: str, db_client: Optional[MongoClient] = None) -> DB:
    """Connect to a collection."""
    if not db_client:
        db_client = get_mongo_client()
    return DB(db=db_client.db, collection_name_1=collection)


def close_DB(db_client: Optional[MongoClient] = None):
    if not db_client:
        db_client = get_mongo_client()
    return db_client._client.close()