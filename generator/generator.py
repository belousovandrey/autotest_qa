from data.data import Person
from faker import Faker
import random

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 80),
        salary=random.randint(10, 100000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )


def generated_file():
    # path = rf'G:\Мой диск\Python\auto_test_qa_notebook\filetest{random.randint(0, 999)}.txt' #указать абсолютный путь до файла
    path = rf'G:\Мой диск\Python\auto_test_qa_notebook\filetest{random.randint(0, 999)}.txt' #указать абсолютный путь до файла
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path
