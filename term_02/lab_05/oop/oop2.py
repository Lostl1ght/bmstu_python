class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def get_info(self):
        print('Имя: {}'.format(self.name))
        print('Фамилия: {}'.format(self.surname))
        print('Квалификация: {}'.format(self.qualification))
        print()

    def __del__(self):
        print('До свидания, мистер {}'.format(self.surname))

persons = [Person('Альберт', 'Смит', 5), Person('Донни', 'Доновиц', 7), Person('Честер', 'Кук', 2)]

for i in range(3):
    min_q = 10
    persons[i].get_info()
    if persons[i].qualification < min_q:
        index = i
        min_q = persons[i].qualification

persons[index].__del__()
input()
