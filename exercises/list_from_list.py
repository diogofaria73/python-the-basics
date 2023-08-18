students = ['João', 8.0, 9.0, 7.0, 'Maria',
            10.0, 8.0, 7.0, 'José', 4.0, 5.0, 6.0, 'Luciano', 9.0, 9.0, 10.0, 'Renatinha', 8.2, 7.7, 6.0]

students_name = []
students_notes = []
students_notes_grouped_by_student = []

for element in students:
    if type(element) == str:
        students_name.append(element)
    else:
        students_notes.append(element)

# create a unique list of students grouped notes by student name
for i in range(len(students_name)):
    students_notes_grouped_by_student.append(
        students_notes[i*3:i*3+3])

print(students_name)
print(students_notes_grouped_by_student)
