#coding:utf-8

import json
import paho.mqtt.client as mqtt

def send_data_via_mqtt(filename, topic, broker, port, username, password):
    # Lire les données à partir du fichier JSON
    with open(filename) as json_file:
        data = json.load(json_file)
    # Initialiser le client MQTT
    client = mqtt.Client()
    client.username_pw_set(username, password)
    # Se connecter au broker MQTT
    client.connect(broker, port)
    # Publier les données sous forme de message JSON
    client.publish(topic, json.dumps(data))
    # Déconnecter le client MQTT
    client.disconnect()
