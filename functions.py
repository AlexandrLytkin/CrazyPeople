import datetime
from random import randint
from termcolor import colored, cprint


class Functions:
    list_of_people = []
    _current_date = datetime.date.today()  # new_current_date = _current_date + datetime.timedelta(days=3300)
    _year_age = 0

    def __init__(self):
        super().__init__()
        self._study = True  # наличие учебы
        self._job = False  # наличие работы
        self._money = 500  # наличные деньги
        self._hungry = 50  # голод
        self._mood = 30  # настроение
        self._health = 100  # здоровье
        self.__day = 1
        self.__flag = True
        Functions.list_of_people.append(self)

    def cycle_of_life(self):
        while self.__flag:
            cprint(f'=========={self.change_data()}=============', color='light_blue')
            self.go_to_eat()
            self.go_to_study()
            if self._hungry <= 20:
                self.go_to_eat()
            dats = randint(1, 6)
            if dats == 1:
                self.go_to_hobby()
            self.go_to_work()
            if self._hungry <= 20:
                self.go_to_eat()
            self.go_to_sleep()
            cprint(f'---------к концу дня----------', color="magenta")
            self.status_of_life()
            self.current_money()
            self.mood_of_people()
            self.mom_money()
            self.change_data()
            self.rise_age()
            self.__day += 1

    def rise_age(self):
        Functions._year_age = self.__day / 365 + self._age
        cprint(f'Мой возраст: {Functions._year_age:0.0f} ', on_color="on_cyan")
        if Functions._year_age == 80:
            cprint(f'Я умираю: {self._name} ', on_color="on_cyan")
            self.__flag = False

    def change_data(self):
        format_date = Functions._current_date + datetime.timedelta(self.__day)
        return format_date.strftime('%d.%m.%Y')

    def mom_money(self):
        if self.__flag and self._study:
            cprint(f'Получил денег от мамы', color='green')
            self._money += 500

    def go_to_eat(self):
        if self.__flag:
            if self._hungry <= 0:
                cprint(f'{self._name} умер от голода', color='red')
                self.__flag = False
            elif 0 < self._hungry <= 70:
                self._hungry += 30
                cprint(f'я поел {self._hungry}', color='green')
            else:
                cprint(f'Я сытый {self._hungry}', color='green')

    def has_study(self):
        if 18 <= Functions._year_age < 25:
            self._study = False
            # cprint(f'не учится {self._study}')
        else:
            self._study = True
            # cprint(f'учится {self._study}')

    def has_job(self):
        if 25 <= Functions._year_age <= 65:
            self._job = True
            return f'работает {self._job}'
        else:
            self._job = False
            return f'не работает {self._job}'

    def mood_of_people(self):
        if self.__flag:
            if self._mood <= 0:
                dats = randint(1, 2)
                if dats == 1:
                    cprint(f'{self._name} повесился', color='red')
                    self.__flag = False
                    del self  # TODO доделать удаление объекта
                else:
                    cprint(f'{self._name} убиться не смог', color='magenta')
                    self._health -= 20
                    self._mood += 10

            elif self._mood <= 20:
                cprint(f'на грани срыва', color='red')
                dats = randint(1, 2)
                if dats == 1:
                    self._mood -= 10
                    cprint(f'{self._name} в глубокой дипресии', on_color='on_red')
                else:
                    cprint(f'{self._name} победил дипресию', on_color="on_green")
                    self._mood += 10

            elif self._mood <= 50:
                cprint(f'обычное настроение', on_color="on_blue")
            elif self._mood == 100:
                cprint(f'отличное настроение', on_color="on_yellow")

    def go_to_work(self):
        self.has_job()
        if self._job:
            cprint(f'Пошел на работу', on_color="on_magenta")
            self._money += 50000
            self._health -= 1
            self._hungry -= 20

    def go_to_study(self):
        self.has_study()
        if self.__flag:
            if self._study:
                cprint(f'Пошел на учебу', color='blue')
                self._mood -= 10
                self._hungry -= 20

    def go_to_hobby(self):

        if self.__flag:
            cprint(f'Занимаюсь хобби', color='cyan')
            self._mood += 5
            self._hungry -= 5
            self._money -= 100

    def status_of_life(self):
        cprint(f'голод:{self._hungry}\n'
               f'здоровье:{self._health}\n'
               f'настроение:{self._mood}\n'
               f'деньги:{self._money}', color='yellow')

    def current_money(self):
        if self.__flag:
            if self._money <= -1000:
                cprint(f'{self._name} убили за долги', color='red')
                self.__flag = False

    def current_health(self):
        if self.__flag:
            if self._health <= 0:
                cprint(f'{self._name} умер от не достатка здоровья', color='red')
                self.__flag = False
            elif self._health >= 100:
                return
            else:
                self._health += 1

    def go_to_sleep(self):
        if self.__flag:
            cprint(f'Сплю', color='blue')
            self._hungry -= 5
            self._health +=10

            if self._mood >= 100:
                return
            else:
                self._mood += 10
            self.current_health()
