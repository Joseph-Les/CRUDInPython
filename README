Animal Shelter CRUD Operations

Project Overview

This project provides a Python module for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database. (Update and Delete is work in progress) The module is designed to be reusable and can be imported into other Python scripts or Jupyter Notebooks. It includes a class, AnimalShelter, that provides methods to interact with a MongoDB collection.

Setup Instructions

Prerequisites
	Python 3.x
	MongoDB server
	pymongo library

Installation
1. Clone the repository:
	git clone https://github.com/your-username/animal-shelter-crud.git
2. Install the required Python packages:
	pip install pymongo
3. Ensure your MongoDB server is running.

Usage

Initialization
The AnimalShelter class is used to interact with the MongoDB collection. You need to initialize it with your MongoDB connection details.
	shelter = AnimalShelter(user='', password='', host='', port=, db='', collection='')

Create Method
The create method inserts a document into the collection.
	new_animal = {
    		"name": "Max",
    		"species": "Dog",
    		"breed": "Golden Retriever",
    		"age": 5,
    		"adopted": False
	}
	insert_success = shelter.create(new_animal)
	print(f"Insert success: {insert_success}")

Read Method
The read method queries for documents in the collection based on a given query.
	query = {"species": "Dog"}
	dogs = shelter.read(query)
	print(f"Found dogs: {dogs}")

Testing
Open a new Jupyter Notebook to Test the CRUD operations. Ensure the test and  animal_shelter files are in the same directly, then insert the test with your DB information. Run test.
