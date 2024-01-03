class Work:
    """ИТ компания"""
    __name = 'IT Company'
    __salary = 0
    __all_employees = []
    __count_employees = 0
    __vacancy = {1: "Junior", 2: 'Middle', 3: 'Senior'}

    def __init__(self, name, vacancy=1):
        self.__name = name
        self.__vacancy = vacancy
        if vacancy in Work.__vacancy:
            self.__vacancy = Work.__vacancy[vacancy]

    def __str__(self):
        return (f'Фирма- {self.__name}.'
                f'\nВсего сотрудников: {self.__count_employees}.'
                f'\nСотрудники:\n' + '\n'.join(str(employee) for employee in self.__all_employees))

    def add_to_work(self, employee):
        Work.__all_employees.append(employee)
        Work.__count_employees += 1
        return self

    def get_all_employees(self):
        return ' '.join(str(employee) for employee in self.__all_employees)

    def dismissed_to_work(self, employee):
        for current in Work.__all_employees:
            if current in employee:
                del self
