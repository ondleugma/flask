from app import app, db, Prepod

def delete_all_prepods():
    with app.app_context():
        # Удаляем все записи из таблицы Prepod
        Prepod.query.delete()

        # Фиксируем изменения в базе данных
        db.session.commit()

if __name__ == "__main__":
    delete_all_prepods()