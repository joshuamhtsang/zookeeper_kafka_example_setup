# zookeeper_kafka_example_setup
An example methodology for setting up a Kafka and Zookeeper system


### Set up a zookeeper.
$ docker pull confluentinc/cp-zookeeper:latest
$ docker run --restart unless-stopped -d --net=host --name=zookeeper-1 \
 -e ZOOKEEPER_SERVER_ID=1 -e ZOOKEEPER_CLIENT_PORT=32181 \
 -e ZOOKEEPER_TICK_TIME=2000 -e ZOOKEEPER_INIT_LIMIT=5 \
 -e ZOOKEEPER_SYNC_LIMIT=2 \
 confluentinc/cp-zookeeper:latest

### Set up a kafka broker.
$ docker pull confluentinc/cp-kafka:latest
$ docker run -d --restart unless-stopped --net=host --name=kafka-1 \
 -e KAFKA_ZOOKEEPER_CONNECT=127.0.0.1:32181 \
 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://127.0.0.1:9093 \
 -e KAFKA_GROUP_MAX_SESSION_TIMEOUT_MS=600000 \
 -e KAFKA_BROKER_ID=1 \
 confluentinc/cp-kafka:latest
