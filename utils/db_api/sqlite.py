import sqlite3




class Database:
    def __init__(self, path_to_db="data/blocking_conditions_db.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_blocking_condition(self, **kwargs):
        sql = "SELECT conditions FROM blocking_conditions WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def select_all(self):
        sql = "SELECT * FROM blocking_conditions"
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
__________________________________________________________________________
Executing
{statement}
_________________________________________________________________________
""")
