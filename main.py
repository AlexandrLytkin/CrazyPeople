import functions
from university import University
from work import Work
from people import People

vasya = People("Vasia", 18, 'мозг')
sveta = People("Sveta", 23, 'мозг')
work = Work('Crazy Brain', 2)
university = University('Hogwards')
University.add_to_student(university, vasya)
University.add_to_student(university, sveta)
print(vasya)
print(30 * '=')
# Work.add_to_work(work, vasya)
# Work.add_to_work(work, sveta)
print(work)
print(30 * '=')
print(university)
print(30 * '+')

for cycle in functions.Functions.list_of_people:
    People.cycle_of_life(cycle)
