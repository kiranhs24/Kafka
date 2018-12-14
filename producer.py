from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('mytopic', key='hello', value='Finally i got the message TY !! ')
p.flush(30)

