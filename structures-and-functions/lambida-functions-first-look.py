# create a list of students notes

students_data = [8, 9, 6, 7.2, 3.1]
qualitative = 0.5

final_notes = map(lambda note: note + qualitative, students_data)

print(list(final_notes))
