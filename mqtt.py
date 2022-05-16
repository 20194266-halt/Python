import paho.mqtt.client as mqtt
import json

MQTT_HOST = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "MQTTBroker"
#Dong goi du lieu
MQTT_MSG=json.dumps({"id":11, "packet_no":126, "temperature":30, "humidity":60, "tds":1100, "pH":5.0});

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)
    print ("Da public du lieu thanh cong")

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) 
    payload = json.loads(msg.payload) 
    print(payload['sepalWidth']) 
    client.disconnect() 

mqttClient = mqtt.Client()

mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

mqttClient.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

mqttClient.loop_forever()
