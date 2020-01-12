# zookeeper_kafka_example_setup
An example methodology for setting up a Kafka and Zookeeper system

##############################################################
## Spin-up Zookeeper and Kafka broker using docker-compose ###
##############################################################
The docker-compose file spins up a single Zookeeper and a single Kafka broker.

$ docker-compose -f docker-compose.yml pull
$ docker-compose up -d

### Create topic called 'JOSH_TOPIC_1'
$ docker exec zookeeper_kafka_example_setup_kafka_1 kafka-topics\
 --create \
 --topic JOSH_TOPIC_1 \
 --zookeeper 127.0.0.1:32181 \
 --partitions 1 \
 --replication-factor 1

### Start a console consumer on topic 'JOSH_TOPIC_1'
$ docker exec zookeeper_kafka_example_setup_kafka_1 kafka-console-consumer\
 --bootstrap-server 127.0.0.1:9093\
 --topic JOSH_TOPIC_1\
 --partition 0\
 --from-beginning

### Create interactive console producer on topic 'JOSH_TOPIC_1'
$ docker exec -it zookeeper_kafka_example_setup_kafka_1 bash
$ kafka-console-producer --topic JOSH_TOPIC_1 --broker-list 127.0.0.1:9093

### Use 'kafka-python' script to send message to topic 'JOSH_TOPIC_1'
$ python3 producer_example.py

See:  https://kafka-python.readthedocs.io/en/master/usage.html
for more details.



#####################################
### Set up without docker-compose ###
#####################################

### Set up a zookeeper ###
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


### Create a topic.
$ docker exec kafka-1 kafka-topics --create --topic JOSH_TOPIC_1 \
--zookeeper 127.0.0.1:32181  --partitions 3 --replication-factor 1


### Check topics.
$ docker exec kafka-1 kafka-topics --describe --zookeeper 127.0.0.1:32181

The output will be like:

Topic:JOSH_TOPIC_1	PartitionCount:3	ReplicationFactor:1	Configs:
	Topic: JOSH_TOPIC_1	Partition: 0	Leader: 1	Replicas: 1	Isr: 1
	Topic: JOSH_TOPIC_1	Partition: 1	Leader: 1	Replicas: 1	Isr: 1
	Topic: JOSH_TOPIC_1	Partition: 2	Leader: 1	Replicas: 1	Isr: 1
Topic:__confluent.support.metrics	PartitionCount:1	ReplicationFactor:1	Configs:retention.ms=31536000000
	Topic: __confluent.support.metrics	Partition: 0	Leader: 1	Replicas: 1	Isr: 1
