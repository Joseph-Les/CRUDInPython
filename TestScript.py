from animal_shelter import AnimalShelter

# Initialize the AnimalShelter instance
shelter = AnimalShelter(user='', password='', host='', port=, db='', collection='')

# Create a new animal document
new_animal = {
    "name": "Max",
    "species": "Dog",
    "breed": "Golden Retriever",
    "age": 5,
    "adopted": False
}
insert_success = shelter.create(new_animal)
print(f"Insert success: {insert_success}")

# Read documents from the collection
query = {"species": "Dog"}
dogs = shelter.read(query)
print(f"Found dogs: {dogs}")

# Update a document in the collection
update_query = {"name": "Max"}
update_values = {"$set": {"age": 6}}
update_success = shelter.update(update_query, update_values)
print(f"Number of documents modified: {update_success}")

# Delete a document from the collection
delete_query = {"name": "Max"}
delete_success = shelter.delete(delete_query)
print(f"Number of documents deleted: {delete_success}")
