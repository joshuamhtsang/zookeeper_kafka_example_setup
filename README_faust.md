faust is, loosely speaking, a Python implementation of Kafka Streams.
Once you have a zookeeper (port 32181) and a kafka broker (port 9093) 
instance running, you can do:

$ faust -A faust_example worker -l info

Send a message to the 'greet' agent:

$ faust -A faust_example send @greet 'Hello!'

Alternatively, send to the 'greetings' topic:

$ faust -A faust_example send greetings 'Ahoy!'

If you replace the rather simplistic 'print()' functionality inside 
the faust agent's function for the 'greetings' topic, you can begin
to see these agents can do much more sophisticated things.  Moreover,
these fault agents can be spun up inside Docker containers for DevOps
convenience.

For example, you may have an NLP engine as a faust agent consuming a
particular Kafka topic, and all the NLP's complicated dependencies are
wrapped-up in a Docker image, from which many containers can be initiated. 