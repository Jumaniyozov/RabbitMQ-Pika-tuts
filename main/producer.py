import pika, json

params = pika.URLParameters('amqps://hirdbdum:l3aEbuyBRtoKbriyUY7hL6_DCltrolWF@barnacle.rmq.cloudamqp.com/hirdbdum')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
