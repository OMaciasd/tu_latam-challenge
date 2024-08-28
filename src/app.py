from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from utils.utils import get_db_connection

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class UsCr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return "Hello, Flask with PostgreSQL!"


@app.route('/test-db-connection', methods=['GET'])
def test_db_connection():
    try:
        with db.engine.connect() as connection:
            return jsonify({"message": "Database connection successful", "status": "success"})
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"})


@app.route('/data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM mytable;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        data = []
        for row in rows:
            data.append({"id": row[0], "name": row[1]})

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50010)
