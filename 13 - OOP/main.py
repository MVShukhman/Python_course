from school import Student, Teacher, Assistant

first_student = Student(
    name='Mark',
    year=1997,
    id=12819381,
    faculty='Computer Science',
    subject_list=['Algebra', 'Calculus', 'Programming']
)

second_student = Student(
    name='Sergey',
    year=2000,
    id=487284,
    faculty='History',
    subject_list=['History', 'Politics', 'Psychology']
)

calculus_teacher = Teacher(
    name='Alexey',
    year=1965,
    id=878713,
    subject='Calculus'
)

calculus_teacher.give_mark(first_student, 5) # Ну а как иначе
calculus_teacher.give_mark(first_student, 4)
calculus_teacher.give_mark(first_student, 5)
calculus_teacher.give_mark(first_student, 2) # В жизни так бывает
calculus_teacher.give_mark(first_student, 5)
calculus_teacher.give_mark(second_student, 5) # Должно вывестись, что такого предмета нет у студента

third_student = Assistant(
    name='Elena',
    year=1999,
    id=712871827,
    faculty='Philosophy',
    subject='History', # Инициализация как для студента, но с предметом, по которому студент может выставлять другим оценки подобно преподавателю
    subject_list=['Philosophy', 'History', 'Ancient literature', 'Calculus'],
)

third_student.give_mark(second_student, 4)
third_student.give_mark(second_student, 5)
third_student.give_mark(second_student, 3)
third_student.give_mark(second_student, 5)
third_student.give_mark(second_student, 5)

calculus_teacher.give_mark(third_student, 5) # Ассистент также подобно остальным студентам получает оценки

first_student.get_marks()
second_student.get_marks()
third_student.get_marks()
