from sqlalchemy import create_engine, text


class CompanyTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):
        sql = text("SELECT * FROM company WHERE deleted_at IS NULL")
        return self.db.execute(sql).fetchall()

    def get_active_companies(self):
        sql = text(
            'SELECT * FROM company WHERE is_active = '
            'true AND deleted_at IS NULL'
        )
        return self.db.execute(sql).fetchall()
