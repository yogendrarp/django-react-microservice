import pika
import json
params = pika.URLParameters("amqps://sgknscuf:WUbB_Bl3EDLCOCfEVs1wCQDxbOw7lhkp@gull.rmq.cloudamqp.com/sgknscuf")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)

    if properties.content_type == "product_created ":
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print('Started consuming')
channel.start_consuming()
channel.close()