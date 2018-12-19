from confluent_kafka import Producer

print("Enter a message here \n")
msg = input()
p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('mytopic', key='hello', value=msg)
p.flush(30)

