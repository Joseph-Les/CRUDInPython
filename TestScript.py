from animal_shelter import AnimalShelter

# Initialize the AnimalShelter instance
shelter = AnimalShelter(user='accuser', password='SNHU1234', host='nv-desktop-services.apporto.com', port=32592, db='AAC', collection='animals')

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