import pika
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_appeal(request):
    appeal = json.dumps(request.data)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
               'rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='appeals')
    channel.basic_publish(exchange='',
                          routing_key='appeals',
                          body=appeal)
    connection.close()

    return Response(['Ваш запрос отправлен'], status=200)
