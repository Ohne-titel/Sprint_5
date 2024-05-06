from faker import Faker


def test_registration_data():
    fake = Faker()
    email = fake.email()

    return email


def test_login_data():
    email = "miagkova.elina@mail.ru"
    password = "123456"

    return email, password
