from faker import Faker


def test_registration_data():
    fake = Faker()
    email = fake.email()

    return email
