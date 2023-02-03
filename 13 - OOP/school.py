from person import Person

class Student(Person): # Студент является человеком, поэтому наследует базовый класс человека
    faculty = None
    marks = None # Оценки будут в виде словаря, где ключом является предмет, значением - список оценок

    def __init__(self, name: str, year: int, id: int, faculty: str, subject_list: list=None) -> None:
        super().__init__(name, year, id) # Сначала запускаем init у класса-родителя чтобы задать базовые параметры человека
        self.faculty = faculty
        self.marks = dict()
        if subject_list is not None: # Если при создании студента указан набор предметов, то также инициализируем их в журнале оценок
            for subject in subject_list:
                self.add_subject(subject)

    
    def add_subject(self, subject: str): # Метод для записи на предмет, т.е. добавление его в журнал для оценок
        self.marks[subject] = list()

    def get_marks(self):
        print(f"{self.name}'s marks:")
        for subject in self.marks.keys():
            print(f'{subject}: {self.marks[subject]}')
    

class Teacher(Person): # Класс преподавателя. Нужен для взаимодействия со студентами
    subject = None # Предмет, который преподаётся. Значение используется для проставления оценок студентам

    def __init__(self, name: str, year: int, id: int, subject: str) -> None:
        super().__init__(name, year, id)
        self.subject = subject

    def give_mark(self, student: Student, mark: int):
        if self.subject not in student.marks: # По предмету, который преподаётся учителем, проверяем, записан ли на него студент
            print('Студент не изучает данный предмет!')
            return
        student.marks[self.subject].append(mark) # Выставляется оценка в журнал студенту
    


class Assistant(Teacher, Student): # Пример наследования - ассистент. Он является как студентом, так и учителем по определённому предмету
    def __init__(self, name: str, year: int, id: int, faculty: str, subject: str, subject_list: list = None) -> None:
        Student.__init__(self, name=name, year=year, id=id, faculty=faculty, subject_list=subject_list) # В данном случае проще всего вызвать конструктор для студента, а поля для учителя заполнить в этом конструкторе
        self.subject = subject # Мы один раз инициализируем имя, id, и остальные параметры, поэтому здесь сначала задали у студента, затем добавили свои поля для учитяля. Можно вызвать и конструктор для учителя, но тогда поля студента нужно будет определять здесь
