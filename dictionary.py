# dict is key with value
# dict=key:value

myDict = {
    "Fast": "In a Quick Manner",
    "Abhii": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'Abhii': 'Player'}
}

# print(myDict['Fast'])
# print(myDict['Abhii'])
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['Abhii'])



myDict = {
    "fast": "In a Quick Manner",
    "Abhii": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Abhii': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Abhii": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Abhii")) # Prints value associated with key "Abhii"
print(myDict["Abhii"]) # Prints value associated with key "Abhii"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("Abhii2")) # Returns None as Abhii2 is not present in the dictionary
print(myDict["Abhii2"]) # throws an error as Abhii2 is not present in the dictionary




 