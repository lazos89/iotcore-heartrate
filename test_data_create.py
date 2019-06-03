#data_file = "./data/SampleData.json"
import json
import time
import random
import datetime


def create_random_date():

    data={
        "deviceID":"dev1",
        "time": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "flow": str(random.uniform(4,12)),
        "battery":"98%",
        "pressure": str(random.uniform(12,16)),
        "temperature": str(random.uniform(16,25)),
    }
    return data
    
# data_file = "./data/SampleData.json"
# fr = open(data_file, 'r')
# i = 1 
while True:
    # print(type(line))
    # data = json.loads(line) 
    #   
    print(type(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))
    data = create_random_date()
    # print(type(data))

    # Publish "payload" to the MQTT topic. qos=1 means at least once
    # delivery. Cloud IoT Core also supports qos=0 for at most once
    # delivery.
    payload = json.dumps(data)    # JSON object to string conversion
    print('Publishing message #{}: \'{}\''.format(i, payload))
    # client.publish(mqtt_topic, payload, qos=1)
    # i += 1

    # time.sleep(0.1)
    time.sleep(random.uniform(0.2,3))
    # time.sleep((random.randint(0.2, 2)))



def test():
    