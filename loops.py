from datetime import datetime

# List structure with a lot of data types
list_of_things = ['a', 'b', 'c', 1, datetime.now(), 1.75]

# In python, you can scroll through a list using some resources, for example:

# Method for -> Most used in python
for thing in list_of_things:
    print(thing)

# Method while -> Used in some cases, specially when you need to control the loop.
stop_loop = False  # define a variable to control the loop.

# While the variable is False, the loop will continue.
while stop_loop != True:
    print('I will never stop to print this message')
    # When the variable is True, the loop will stop. In this case, the loop will run only once.
    stop_loop = True

# In a real situation, you can use while loop, to receive a lot of inputs of users,
# and stop the input loop when users type a specific value.
# For example:

do_you_want_to_continue = 'exit'

while do_you_want_to_continue:
    do_you_want_to_continue = input(
        'Do you want to continue? (type exit to stop): ')
    print('You typed: ', do_you_want_to_continue)

    if do_you_want_to_continue == 'exit':
        print('You typed exit, so the loop will stop here.')
        break  # break the loop
