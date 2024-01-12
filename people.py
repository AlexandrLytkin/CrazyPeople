from functions import Functions


class People(Functions):

    def __init__(self, name, age, in_head=None):
        super().__init__()
        self.life = True
        self._age = age  # возраст
        self._name = name  # имя
        if in_head == 'мозг':
            self._in_head = in_head  # мозг есть
        else:
            self._in_head = 'мозга нет'  # мозга нет

    def get_age(self):
        print(self._age)
        return self._age

    def __str__(self):
        return f'Имя: {self._name} возраст: {self._age}'
