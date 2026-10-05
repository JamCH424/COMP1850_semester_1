# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["RandomRiver1"]= "RandomLocation1"
rivers["RandomRiver2"]= "RandomLocation2"

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print("\n")
print(rivers.items())

# Delete an entry from the rivers database
rivers.pop("RandomRiver1")
print(rivers)