import pika

params = pika.URLParameters("amqps://sgknscuf:WUbB_Bl3EDLCOCfEVs1wCQDxbOw7lhkp@gull.rmq.cloudamqp.com/sgknscuf")
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method=None, body=None):
    print("somethin")
    channel.basic_publish(exchange='', routing_key='main', body='hello')