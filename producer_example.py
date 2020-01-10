from kafka import KafkaProducer

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:32181', acks=1,
                             value_serializer=lambda m: json.dumps(m).encode('ascii'),
                             retries=2, max_request_size=2 * 1024 * 1024,
                             request_timeout_ms=3000)
