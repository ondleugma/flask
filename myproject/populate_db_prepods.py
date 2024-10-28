from app import app, db, Prepod
from faker import Faker
from datetime import datetime

fake = Faker('ru_RU')  # Устанавливаем локализацию на русский язык

def create_fake_prepods(count=100):
    with app.app_context():
        for _ in range(count):
            prepod = Prepod(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                middle_name=fake.middle_name_male(),  # Используем middle_name_male для middle_name
                age=fake.random_int(min=18, max=30),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=30),
                is_active=fake.boolean(),
                salary=fake.random_int(min=1000, max=5000),
                address=fake.address()
            )
            db.session.add(prepod)
        db.session.commit()

if __name__ == "__main__":
    create_fake_prepods()