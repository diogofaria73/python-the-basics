# List of temperatures in celsius degrees
temp_in_celsius = [0, 25, 37, 38, 100]

# Convert celsius to fahrenheit using a lambda function.
# Formula: (9/5) * celsius + 32 -> fahrenheit.
# We are using map to apply the lambda function to each element of the list.
# In the end of the process, we are converting the map object to a list and return the
# result to the temp_in_fahrenheit variable.
temp_in_fahrenheit = list(map(lambda celsius: (
    (9/5) * celsius) + 32, temp_in_celsius))

# Print the final result after convert temperatures.
print(temp_in_fahrenheit)
