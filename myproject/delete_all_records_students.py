from app import app, db, Student

def delete_all_records():
    with app.app_context():
        # Удаляем все записи из таблицы Student
        Student.query.delete()

        # Фиксируем изменения в базе данных
        db.session.commit()

if __name__ == "__main__":
    delete_all_records()