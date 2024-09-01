import pika


def callback(
    ch,
    method,
    properties,
    body
):
    print(
        f"Returning: {body}"
    )


def consume_log(
        message
):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'localhost'
        )
    )

    channel = connection.channel(
    )

    channel.exchange_declare(
        exchange='logs', exchange_type='fanout'
    )

    result = channel.queue_declare(
        queue='',
        exclusive=True
    )

    queue_name = result.method.queue

    channel.queue_bind(
        exchange='logs',
        queue=queue_name
    )

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


consume_logs()
