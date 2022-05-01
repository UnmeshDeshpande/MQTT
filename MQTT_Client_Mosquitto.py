import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#broker_address="10.2.167.173"
broker_address="test.mosquitto.org"
print("creating new instance")
client = mqtt.Client("UnmeshPC") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","mosquitto/test1")
client.subscribe("mosquitto/test2")
print("Publishing message to topic","mosquitto/test2")
client.publish("mosquitto/test2","OFF")
time.sleep(4) # wait
client.loop_stop() #stop the loop