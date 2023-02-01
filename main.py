#!/usr/env/python3
#coding:utf-8

import ctypes, os, time, json, smartcard
from smartcard.System import readers

currentUser = os.environ["USERNAME"]

def create_folder():
    global folder_path
    folder_path = "C:\\Users\\{}\\AppData\\Local\\Programs\\WinLockerRFID".format(currentUser)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass

def lock_computer():
    ctypes.windll.user32.LockWorkStation()

def init_rfid():
    global uid
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
    uid = "".join([format(x, "02x") for x in data])

def write_to_log(log_file, log_message):
    try:
        with open(log_file, 'w') as file:
            file.write(log_message)
    except FileNotFoundError:
        with open(log_file, 'w') as file:
            file.write(log_message)

CardMissing = "Missing"
UserCard = {"01020304": "BAGDE_NAME", "01020304": "BAGDE_NAME", "01020304": "BAGDE_NAME"}

create_folder()
CardPresentLog = "{}\CardPresentLog.txt".format(folder_path)
ProfileCardLog = "{}\ProfileCardLog.txt".format(folder_path)

while True:
    time.sleep(1)
    try:
        init_rfid()
        time.sleep(0.5)
        if(uid == "01020304") or (uid == "01020304"):
            write_to_log(CardPresentLog, uid)
            write_to_log(ProfileCardLog, UserCard[uid])
            pass
        else:
            write_to_log(CardPresentLog, "No Profile")
            write_to_log(ProfileCardLog, CardMissing)
            lock_computer()
    except KeyboardInterrupt:
        exit()
    except:
        write_to_log(CardPresentLog, CardMissing)
        write_to_log(ProfileCardLog, "No Profile")
        lock_computer()
        pass
