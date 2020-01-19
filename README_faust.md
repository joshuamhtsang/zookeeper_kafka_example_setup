faust is, loosely speaking, a Python implementation of Kafka Streams.
Once you have a zookeeper (port 32181) and a kafka broker (port 9093) 
instance running, you can do:

$ faust -A faust_example worker -l info

