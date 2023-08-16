import matplotlib.pyplot as plt
from random import choice
from math import ceil

students = ['John', 'Mary', 'Mike', 'Jane', 'Alex']
notes = [5, 6, 7, 8, 9]

plt.title('Notes of students')
plt.bar(students, notes)
plt.axes().get_xaxis().set_visible(False)
plt.show()
