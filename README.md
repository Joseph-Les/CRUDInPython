# Animal Shelter CRUD Operations

**Project Overview**

This repository provides a Python module for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database. The module is designed to be reusable and can be imported into other Python scripts or Jupyter Notebooks. It includes a class, AnimalShelter, that provides methods to interact with a MongoDB collection.

**Purpose**

The purpose of this CRUD Python module is to offer a simplified interface for interacting with MongoDB databases, specifically for the management of an animal shelter's data. This module allows users to create, read, update, and delete records in a MongoDB collection, making it easier to manage animal records programmatically.

**Python Driver for MongoDB**

The Python driver used for MongoDB in this project is pymongo. It was chosen because it is the official MongoDB driver for Python, providing a comprehensive and efficient interface for interacting with MongoDB databases. pymongo supports all MongoDB operations and provides a robust way to handle database interactions in Python.

**Setup Instructions**

Prerequisites
1. Python 3.x
2. MongoDB server
3. `pymongo` library

**Installation**
1. Clone the repository:
	```git clone git@github.com:Joseph-Les/CRUDInPython.git```
2. Install the required Python packages:
	```pip install pymongo```
3. Ensure your MongoDB server is running.


**Usage - Initialization**

The AnimalShelter class is used to interact with the MongoDB collection. You need to initialize it with your MongoDB connection details.

	shelter = AnimalShelter(user='', password='', host='', port=, db='', collection='')

**Create Method**

The create method inserts a document into the collection.
	
	def create(self, data):
        if data is not None and isinstance(data, dict):
            try:
                self.database.animals.insert_one(data)
                return True
            except OperationFailure as e:
                print(f"Could not insert document: {e}")
                return False
        else:
            raise ValueError("Data must be a dictionary and not None")

**Read Method**

The read method queries for documents in the collection based on a given query.

	def read(self, query):
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

**Update Method**

The update method queries for document(s) in the collection based on query, then updates the given value(s)

	 if query is not None and isinstance(query, dict) and update_values is not None and isinstance(update_values, dict):
            try:
                if update_many:
                    result = self.collection.update_one(query, update_values)
                else:
                    result = self.collection.update_one(query, update_values)
                return result.modified_count
            except OperationFailure as e:
                print(f"Could not update document(s): {e}")
                return 0
        else:
            raise ValueError("Query and update values must be dictionaries and not None")

**Delete Method**

The delete method queries for document(s) in the collection based on the query, then deletes the given value(s)

	if query is not None and isinstance(query, dict):
            try:
                if delete_many:
                    result = self.collection.delet_many(query)
                else:
                    result = self.collection.delete_one(query)
                return result.deleted_count
            except OperationFailure as e:
                print(f"Could not delete document(s): {e}")
                return e
        else:
            raise ValueError("Query must be a dictionary and not None")

**Testing**

To ensure the functionality of the module, follow these steps to test it using a Jupyter Notebook.

1. Ensure your MongoDB server is running. Gather your database name and the user credentials..
   
	1A. Create a new user (optional):

    	db.createUser ({ 
			user: "<name of the user>",
			pwd: "<password>",
			roles [( role: "readWrite", db: "<name of database>" }]
		})
   
2. Start a new Jupyter Notebook.
3. Insert the test script into the first cell of the Jupyter Notebook. Replace user, password, host, port, db, and collection with your own user information.
4. Edit the Create and Read methods to match your collection if using a different database structure.
5. Create a Python script within the same directory as your Jupyter Notebook, named animal_shelter.py, containing the AnimalShelter class definition.
6. Execute the code in the Jupyter Notebook to test the Create and Read functionalities.'

By following these instructions, you should be able to reproduce and test the functionality of the Animal Shelter CRUD operations module.

**Example**

![Screenshot 2024-06-03 at 8 12 18 PM](https://github.com/Joseph-Les/CRUDInPython/assets/84045743/52f22e7e-29c7-47ee-932b-2465e24d1ea4)

