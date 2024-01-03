from functions import Functions


class People(Functions):

    def __init__(self, name, age, in_head=None):
        super().__init__()
        self._age = age  # возраст
        self._name = name  # имя
        if in_head == 'мозг':
            self._in_head = in_head  # мозг есть
        else:
            self._in_head = 'мозга нет'  # мозга нет

    def __str__(self):
        return f'Имя: {self._name} возраст: {self._age}'
