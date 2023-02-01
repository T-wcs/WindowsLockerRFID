#!/usr/env/python3
#coding:utf-8

import os, time, json, smartcard
from smartcard.System import readers
from modules import computerLocker, folderCreate, jsonData

currentUser = os.environ["USERNAME"]
folder_path = "C:\\Users\\{}\\AppData\\Local\\Programs\\WinLockerRFID".format(currentUser)
CardGrantedConfig = "{}\CardGranted.json".format(folder_path)

def init_rfid():
    global card_uid
    # Recherchez tous les lecteurs disponibles
    r = smartcard.System.readers()
    # Sélectionnez le lecteur WCR330 => la partie NFC/RFID / La partie CARTE A PUCE 0
    reader = r[1]
    # Connectez-vous au lecteur
    connection = reader.createConnection()
    connection.connect()
    # Envoyez la commande APDU pour obtenir l'UID
    data, sw1, sw2 = connection.transmit([0xFF, 0xCA, 0x00, 0x00, 0x00])
    # Affichez l'UID de la carte
    card_uid = "".join([format(x, "02x") for x in data])

folderCreate.create_folder()
while True:
    time.sleep(1)
    try:
        init_rfid()
        time.sleep(0.5)
        result = jsonData.check_uid(CardGrantedConfig, card_uid)
        if(result):
            jsonData.write_to_json_file(card_uid, currentUser)
            pass
        else:
            jsonData.write_to_json_file("Missing", "No Profile")
            computerLocker.lock_computer()
    except KeyboardInterrupt:
        exit()
    except:
        jsonData.write_to_json_file("Missing", "No Profile")
        computerLocker.lock_computer()
        pass
