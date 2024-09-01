from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pika
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables desde el archivo .env

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')
RABBITMQ_URL = os.getenv('RABBITMQ_URL')

engine = create_engine(DATABASE_URL)

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue='data_queue')


@app.route('/')
def homepage():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
