import pika
import json
from main import Product, db, app
params = pika.URLParameters("amqps://sgknscuf:WUbB_Bl3EDLCOCfEVs1wCQDxbOw7lhkp@gull.rmq.cloudamqp.com/sgknscuf")
params.heartbeat = 300
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(data)
    print(properties.content_type)
    with app.app_context():
        if properties.content_type == "product_created":
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            db.session.add(product)
            db.session.commit()
        elif properties.content_type == "product_updated":
            product = Product.query.get(data["id"])
            product.title = data["title"]
            product.image = data["image"]
            db.session.commit()
        elif properties.content_type == "product_deleted":
            product = Product.query.get(int(data))
            db.session.delete(product)
            db.session.commit()

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started consuming')
channel.start_consuming()
channel.close()