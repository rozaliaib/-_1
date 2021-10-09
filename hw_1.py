class People:
    age=''

class Students(People):
    def __init__(self, name):
        self.name = name

study = 'School'

student1 = Students('Sasha')
student1.age = 16
print("Student's name is", student1.name, '.', 'He is', student1.age, '.', 'He study at', study, '.')

student2 = Students('Olya')
student2.age = 17
print("Student's name is", student2.name, '.'  'She is', student2.age, 'He study at', study, '.')

student3 = Students('Ira')
student3.age = 15
print("Student's name is", student3.name, '.'  'She is', student3.age, 'He study at', study, '.')

student4 = Students('Sasha')
student4.age = 18
print("Student's name is", student4.name, '.'  'She is', student4.age, 'She study at', study, '.')

student5 = Students('Zoya')
student5.age = 15
print("Student's name is", student5.name, '.'  'She is', student5.age, 'She study at', study, '.')

student6 = Students('Alex')
student6.age = 16
print("Student's name is", student6.name, '.'  'He is', student6.age, 'He study at', study, '.')

student7 = Students('Aliya')
student7.age = 17
print("Student's name is", student7.name, '.'  'She is', student7.age, 'She study at', study, '.')

student8 = Students('Eva')
student8.age = 18
print("Student's name is", student8.name, '.'  'She is', student8.age, 'She study at', study, '.')


class Adults(People):
    def __init__(self, name):
        self.name = name

work = ''

adult1 = Adults('Sergey')
adult1.age = 42
adult1.work = 'doctor'
print("Adult's name is", adult1.name, '.', 'He is', adult1.age, '.', 'He is', adult1.work, '.')

adult2 = Adults('Vitaliy')
adult2.age = 40
adult2.work = 'fireman'
print("Adult's name is", adult2.name, '.', 'He is', adult2.age, '.', 'He is', adult2.work, '.')

adult3 = Adults('Anastasia')
adult3.age = 45
adult3.work = 'manager'
print("Adult's name is", adult3.name, '.', 'She is', adult3.age, '.',  'She is', adult3.work, '.')

adult4 = Adults('Marta')
adult4.age = 47
adult4.work = 'nurse'
print("Adult's name is", adult4.name, '.', 'She is', adult4.age, '.', 'She is', adult4.work, '.')

adult5 = Adults('Sonya')
adult5.age = 38
adult5.work = 'hairdresser'
print("Adult's name is", adult5.name, '.', 'She is', adult5.age, '.', 'She is', adult5.work, '.')

adult6 = Adults('Pavel')
adult6.age = 41
adult6.work = 'engineer'
print("Adult's name is", adult6.name, '.', 'He is', adult6.age, '.', 'He is', adult6.work, '.')

adult7 = Adults('Vanya')
adult7.age = 43
adult7.work = 'policeman'
print("Adult's name is", adult7.name, '.', 'He is', adult7.age, '.', 'He is', adult7.work, '.')

adult8 = Adults('Veronika')
adult8.age = 49
adult8.work = 'dancer'
print("Adult's name is", adult8.name, '.', 'She is', adult8.age, '.', 'She is', adult8.work, '.')



