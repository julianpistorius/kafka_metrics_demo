import json
import kafka

consumer = kafka.KafkaConsumer('glances', bootstrap_servers=['192.168.72.2:9092'], value_deserializer=json.loads)

for s in consumer:
    print(s)
