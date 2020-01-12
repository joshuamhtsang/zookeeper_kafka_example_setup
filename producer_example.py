from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import sys

if __name__ == '__main__':
    # Make KafkaProducer object.
    producer = KafkaProducer(
        bootstrap_servers=['127.0.0.1:9093'],
        value_serializer=lambda m: json.dumps(m).encode('ascii')
    )

    # Asynchronous by default
    future = producer.send('JOSH_TOPIC_1', {"key": "value"})
    print(type(future))

    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError as e:
        print("Sorry, something went wrong!")
        raise e

    # Successful result returns assigned partition and offset
    print("Topic: ", record_metadata.topic)
    print("Partition: ", record_metadata.partition)
    print("Offset: ", record_metadata.offset)
