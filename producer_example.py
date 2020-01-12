from kafka import KafkaProducer
import json

if __name__ == '__main__':
    # Make KafkaProducer object.
    producer = KafkaProducer(
        bootstrap_servers='127.0.0.1:9092',
        acks=1,
        value_serializer=lambda m: json.dumps(m).encode('ascii'),
        retries=2,
        max_request_size=2*1024*1024,
        request_timeout_ms=3000
    )

    producer.send('JOSH_TOPIC_1', value={'event': 'click'})
