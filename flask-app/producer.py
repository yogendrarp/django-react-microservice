import pika
import json

params = pika.URLParameters("amqps://sgknscuf:WUbB_Bl3EDLCOCfEVs1wCQDxbOw7lhkp@gull.rmq.cloudamqp.com/sgknscuf")
params.heartbeat = 300

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method=None, body=None):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)