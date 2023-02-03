class Person: # Базовый класс, от которого будут наследоваться остальные классы, связанные с людьми
    name = ''
    year_of_birth = ''
    pasport_id = 0

    def __init__(self, name: str, year: int, id: int) -> None:
        self.name = name
        self.year_of_birth = year
        self.pasport_id = id
    
    def identify(self): # Пример метода, который вне зависимости от професии/деятельности присущ каждому человеку, поэтому объявлен в базовом классе
        print(f'Name: {self.name}')
        print(f'Pasport id: {self.pasport_id}')
        print(f'Born: {self.year_of_birth}')
