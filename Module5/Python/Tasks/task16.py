
# Module 3b Task 16

#Declare a dictionary with any key-value pair of items/elements
places = {
    "Nigeria": "Abuja",
    "England": "London",
    "Ghana": "Accra",
    "France": "Paris"
}

#Print the dictionary in console
print("Dictionary:", places)

#Update the dictionary with two different key-value pair items
places.update({"Canada": "Ontario", "America": "New York"})

#Print the dictionary in console again
print("Dictionary update:", places)

#Note: you can experiment with the other list functions too in the task.
# pop
places.pop("Ghana")
print("pop:", places)

# values
places_values = places.values()
print("values:", places_values)

# keys
places_keys = places.keys()
print("keys:", places_keys)

# copy
copied_places = places.copy()
print("copy:", copied_places)

# clear
places.clear()
print("clear:", places)
print("copied places:", copied_places)