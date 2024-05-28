from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password, host, port, db, collection):

        """Initialize the MongoClient and set the database and collection"""
        try:
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
            self.database = self.client[db]
            self.collection = self.database[collection]
        except ConnectionFailure as e:
            raise Exception(f"Could not connect to MongoDB: {e}")

    def create(self, data):
        """
        Inserts a document into the collection.
        :param data: A dictionary containing the key/value pairs for the document
        :return: True if insert is successful, else False.
        """
        if data is not None and isinstance(data, dict):
            try:
                self.database.animals.insert_one(data)
                return True
            except OperationFailure as e:
                print(f"Could not insert document: {e}")
                return False
        else:
            raise ValueError("Data must be a dictionary and not None")

    def read(self, query):
        """
        Queries for documents in the collection.
        :param query: A dictionary containing the key/value lookup pairs.
        :return: A list of documents that match the query, else an empty list.
        """
        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                result = list(cursor)
                return result
            except OperationFailure as e:
                print(f"Could not retrieve documents: {e}")
                return []
        else:
            raise ValueError("Query must be a dictionary and not None")
