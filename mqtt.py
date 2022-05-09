import paho.mqtt.client as mqtt
import json

MQTT_HOST = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "LaThiHa"

MQTT_MSG=json.dumps({"id":11, "packet_no":126, "temperature":30, "humidity":60, "tds":1100, "pH":5.0});

def on_publish(client, userdata, mid):
    print ("Public thanh cong")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) 
    payload = json.loads(msg.payload) 
    print(payload['sepalWidth']) 
    client.disconnect() 

mqttc = mqtt.Client()

mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

mqttc.loop_forever()
