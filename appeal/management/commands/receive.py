import pika
import json
from appeal.models import Client, Appeal
from django.core.management.base import BaseCommand


def callback(ch, method, properties, body):
    appeal = json.loads(body)
    client = Client(
        name=appeal['name'],
        surname=appeal['surname'],
        patronymic=appeal['patronymic'],
        phone=appeal['phone'],
     )
    client.save()
    appeal_bd = Appeal(description=appeal['message'], client=client)
    appeal_bd.save()
    print('обращение клиента отправленно в бд')


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                   'rabbit'))
        channel = connection.channel()
        channel.queue_declare(queue='appeals')
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.basic_consume('appeals', callback, auto_ack=True)

        channel.start_consuming()


if __name__ == "__main__":
    Command().handle()
