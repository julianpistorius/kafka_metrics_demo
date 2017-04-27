import json

import kafka

consumer = kafka.KafkaConsumer('metricsets', bootstrap_servers=['192.168.72.2:9092'], value_deserializer=json.loads)

for index, record in enumerate(consumer):
    print(index, record.timestamp, record.value)
    if index > 10:
        break
