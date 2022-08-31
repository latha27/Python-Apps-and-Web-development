students = [("Allen Anderson", "Computer Science"),
            ("Edgar Einstein", "Engineering"),
            ("Farrah Finn", "Fine Arts")]


def add_new_student(students, name, major):
    students.append((name, major))
    return students


def update_student(students, index, name, major):
    students[index] = name, major
    return students


def find_students_by_name(students, name):
    return [student for student in students if name in student[0]]


def get_all_majors(students):
    return [student[1] for student in students]

print(add_new_student(students=students,name='Latha', major='CA'))
print(update_student(students=students,index=0, name='Suma', major='Arts'))
print(find_students_by_name(students=students, name='Ed'))
print(get_all_majors(students))