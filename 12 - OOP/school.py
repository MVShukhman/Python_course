class Student:
    name = 'Username'
    year_of_birth = 0
    faculty = 'Default'
    
    def __init__(self, name: str, facult: str, year: int) -> None: # Конструктор, который выполняется при создании объекта
        self.name = name
        self.year_of_birth = year
        self.faculty = facult
    
    def say_hi(self): # Все методы, работающие с конкретным объектом, содержат аргумент self - ссылку на вызывающий данный метод объект
        print(f'Hello! My name is {self.name} and I study {self.faculty}')