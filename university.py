class University:
    """Университет"""
    __name = "Университет"
    __all_students = []
    __count_students = 0
    __grants = 0  # стипендия

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return (f'Университет- {self.__name}.'
                f'\nВсего учеников: {self.__count_students}.'
                f'\nУченики:\n' + '\n'.join(str(study) for study in self.__all_students))

    def add_to_student(self, student):
        University.__all_students.append(student)
        University.__count_students += 1
        return self

    def get_all_students(self):
        return '\n'.join(str(student) for student in self.__all_students)

    def dismissed_to_student(self, student):
        for current in University.__all_students:
            if current in student:
                del self
