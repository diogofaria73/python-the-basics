students_data = {'1 Trimestre': 8.5, '2 Trimestre': 7.8, '3 Trimestre': 9.0}


def calculate_average(data):
    total = 0
    for key in data:
        total += data[key]
    return total / len(data)


print(calculate_average(students_data))


#
