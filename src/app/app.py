from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pika
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')
RABBITMQ_URL = os.getenv('RABBITMQ_URL')

engine = create_engine(DATABASE_URL)

def create_rabbitmq_connection(url):
    connection = pika.BlockingConnection(
        pika.URLParameters(
            url
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue='data_queue')
    return connection, channel

if RABBITMQ_URL:
    connection, channel = create_rabbitmq_connection(
        RABBITMQ_URL
    )
else:
    connection, channel = None, None

@app.route('/')
def homepage():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
