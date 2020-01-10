#!/bin/bash

docker exec zookeeper_kafka_example_setup_kafka_1 kafka-topics --describe --zookeeper 127.0.0.1:32181
docker exec zookeeper_kafka_example_setup_kafka_1 kafka-topics --create --topic JOSH_TOPIC_1 --zookeeper 127.0.0.1:32181 --partitions 3 --replication-factor 1
docker exec zookeeper_kafka_example_setup_kafka_1 kafka-topics --describe --zookeeper 127.0.0.1:32181

docker exec zookeeper_kafka_example_setup_kafka_1 kafka-topics --delete --topic JOSH_TOPIC_1 --zookeeper 127.0.0.1:32181
