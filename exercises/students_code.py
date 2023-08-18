import random

students_with_identification_code = []
students_list = ['joão', 'Maria', 'José', 'luciano', 'Renata']


def generate_code(student_name):
    code = str(str(student_name[0])).upper()+str(random.randint(1, 999))
    return code


for student in students_list:
    students_with_identification_code.append([student, generate_code(student)])

print(students_with_identification_code)
