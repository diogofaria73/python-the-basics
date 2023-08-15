from datetime import datetime

# In python are different types of variables, their types are defined by the value assigned to them, for example:
name = 'Diogo Faria'  # this is a string
age = 35  # this is a integer
height = 1.75  # this is a float
weight = 80  # this is a integer
eyes = 'brown'  # this is a string
birth_date = datetime.strptime('1988-09-15', '%Y-%m-%d')  # this is a datetime

# To check their types, you can use the function type().
# This function returns the type of the variable passed as argument.
print(type(name))
print(type(age))
print(type(height))
print(type(weight))
print(type(eyes))
print(type(birth_date))

#
