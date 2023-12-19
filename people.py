class People:

    def __init__(self, age, name, in_head=None):
        self._age = age  # возраст
        self._name = name  # имя
        if in_head == 'мозг':
            self._in_head = in_head  # мозг есть
        else:
            self._in_head = 'мозга нет'  # мозга нет
        self._cash = 500  # наличные деньги
        self._has_job = False  # наличие работы
        self._hungry = 100  # голод
        self._health = 100  # здоровье
        self._study = True  # наличие учебы
        self._mood = 50  # настроение



    def __str__(self):
        return (f'age: {self._age}\n'
                f'name: {self._name}\n'
                f'in head: {self._in_head}')


vasya = People(24, 'Vasya', 'мозг')
print(vasya)

