import collections
import json

import kafka


def write_file(records):
    with open('metrics.csv', 'w') as f:
        for a_record in records:
            f.write('{},{}\n'.format(*a_record))


if __name__ == '__main__':
    consumer = kafka.KafkaConsumer('metricsets', bootstrap_servers=['192.168.72.2:9092'], value_deserializer=json.loads)

    buffer = collections.deque(maxlen=100)
    for index, record in enumerate(consumer):
        value = record.value
        if value.get('metricset', {}).get('module') == 'system' and value.get('metricset', {}).get('name') == 'cpu':
            total_cpu = value['system']['cpu']['system']['pct'] + record.value['system']['cpu']['user']['pct']
            cpu_reading = (record.timestamp, total_cpu,)
            buffer.append(cpu_reading)
            write_file(buffer)
