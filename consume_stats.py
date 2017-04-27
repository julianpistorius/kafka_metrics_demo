import json
import pprint

import kafka

consumer = kafka.KafkaConsumer('metricsets', bootstrap_servers=['192.168.72.2:9092'], value_deserializer=json.loads)

for s in consumer:
    pprint.pprint(s)
