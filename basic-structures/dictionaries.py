# Dictionary, is a data structure that stores data as key-value pairs.
# This kind of structure is also known as an associative array, map, or hash table.
# Dictionaries are indexed by keys, which can be any immutable type;
# strings and numbers can always be keys.
employee = {'name': 'Chris', 'city': 'Seattle',
            'cake': 'Chocolate', 'age': 23, 'salary': 15000}

# Print the dictionary if elements define before
print(employee)

# Add a new key, value pair to the dictionary
employee['level'] = 'Senior'

# Print the dictionary with the new key, value pair
print(employee)

# To remove a key from a dictionary, use the del statement or the pop() method
del employee['level']
employee.pop('salary')


# Print the dictionary without deleted element
print(employee)
