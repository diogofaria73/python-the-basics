list_to_process = [16, 14, 63, 65, 17, 99, 70,
                   11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

list_size = len(list_to_process)

min_value, max_value = list(
    map(lambda x: (min(list_to_process), max(list_to_process)), list_to_process))[0]

total_from_list = sum(list_to_process)

print(f'The list has {list_size} elements, from these elements the bigger value is {max_value} and the minimum value is {min_value}. The total sum of all elements from list is {total_from_list}.')
