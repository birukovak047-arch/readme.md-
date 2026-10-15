import random
from students_table import StudentsTable


DB_CONNECTION_STRING = "postgresql://postgres:kotiki58@localhost:5432/QA"
db = StudentsTable(DB_CONNECTION_STRING)


def unique_keys():
    """
    Возвращает уникальную пару (user_id, subject_id), которой
    точно нет в таблице student. Используем MAX(...)+1 + случайный
    сдвиг, чтобы не пересекаться с реальными данными и между запусками.
    """
    user_id = db.get_next_user_id() + random.randint(0, 10_000)
    subject_id = db.get_next_subject_id() + random.randint(0, 10_000)
    return user_id, subject_id


# ---------- ДОБАВЛЕНИЕ ----------
def test_add_student():
    user_id, subject_id = unique_keys()
    level = "bachelor"
    education_form = "full-time"

    try:
        db.create(user_id, subject_id, level, education_form)

        rows = db.get_by_keys(user_id, subject_id)
        assert len(rows) == 1
        assert rows[0]["user_id"] == user_id
        assert rows[0]["subject_id"] == subject_id
        assert rows[0]["level"] == level
        assert rows[0]["education_form"] == education_form
    finally:
        db.delete(user_id, subject_id)

    assert len(db.get_by_keys(user_id, subject_id)) == 0


# ---------- ИЗМЕНЕНИЕ ----------
def test_update_student():
    user_id, subject_id = unique_keys()

    try:
        db.create(user_id, subject_id, "bachelor", "full-time")

        db.update(user_id, subject_id, "master", "part-time")

        rows = db.get_by_keys(user_id, subject_id)
        assert len(rows) == 1
        assert rows[0]["level"] == "master"
        assert rows[0]["education_form"] == "part-time"
    finally:
        db.delete(user_id, subject_id)

    assert len(db.get_by_keys(user_id, subject_id)) == 0


# ---------- УДАЛЕНИЕ ----------
def test_delete_student():
    user_id, subject_id = unique_keys()
    db.create(user_id, subject_id, "bachelor", "full-time")

    assert len(db.get_by_keys(user_id, subject_id)) == 1

    db.delete(user_id, subject_id)

    assert len(db.get_by_keys(user_id, subject_id)) == 0
