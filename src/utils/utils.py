from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_db_connection():
    try:
        with db.engine.connect() as connection:
            return connection
    except Exception as e:
        raise RuntimeError("Database connection error: " + str(e))
