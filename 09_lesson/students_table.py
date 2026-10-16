from sqlalchemy import create_engine, text


class StudentsTable:
    __scripts = {
        "select by keys": text(
            "SELECT * FROM student "
            "WHERE user_id = :user_id AND subject_id = :subject_id"
        ),
        "insert": text(
            "INSERT INTO student (user_id, subject_id, level, education_form) "
            "VALUES (:user_id, :subject_id, :level, :education_form)"
        ),
        "update": text(
            "UPDATE student "
            "SET level = :level, education_form = :education_form "
            "WHERE user_id = :user_id AND subject_id = :subject_id"
        ),
        "delete by keys": text(
            "DELETE FROM student "
            "WHERE user_id = :user_id AND subject_id = :subject_id"
        ),
        "max user_id": text(
            "SELECT COALESCE(MAX(user_id), 0) FROM student"),
        "max subject_id": text(
            "SELECT COALESCE(MAX(subject_id), 0) FROM student"),
    }

    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string)

    def get_by_keys(self, user_id: int, subject_id: int):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select by keys"],
            {"user_id": user_id, "subject_id": subject_id},
        )
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_next_user_id(self) -> int:
        conn = self.__db.connect()
        value = conn.execute(self.__scripts["max user_id"]).scalar()
        conn.close()
        return int(value) + 1

    def get_next_subject_id(self) -> int:
        conn = self.__db.connect()
        value = conn.execute(self.__scripts["max subject_id"]).scalar()
        conn.close()
        return int(value) + 1

    def create(self, user_id: int, subject_id: int,
               level: str, education_form: str):
        conn = self.__db.connect()
        transaction = conn.begin()
        conn.execute(
            self.__scripts["insert"],
            {
                "user_id": user_id,
                "subject_id": subject_id,
                "level": level,
                "education_form": education_form,
            },
        )
        transaction.commit()
        conn.close()

    def update(self, user_id: int, subject_id: int,
               level: str, education_form: str):
        conn = self.__db.connect()
        transaction = conn.begin()
        conn.execute(
            self.__scripts["update"],
            {
                "user_id": user_id,
                "subject_id": subject_id,
                "level": level,
                "education_form": education_form,
            },
        )
        transaction.commit()
        conn.close()

    def delete(self, user_id: int, subject_id: int):
        conn = self.__db.connect()
        transaction = conn.begin()
        conn.execute(
            self.__scripts["delete by keys"],
            {"user_id": user_id, "subject_id": subject_id},
        )
        transaction.commit()
        conn.close()
