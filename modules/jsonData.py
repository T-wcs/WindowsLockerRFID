#!/usr/env/python3
#coding:utf-8

import json, os

currentUser = os.environ["USERNAME"]
folder_path = "C:\\Users\\{}\\AppData\\Local\\Programs\\WinLockerRFID".format(currentUser)
OutputJsonLog = "{}\output.json".format(folder_path)

def write_to_json_file(card_uid, card_profile):
    # Définir les données à écrire dans le fichier
    data = {
        "Status": {
            "CardUID": card_uid,
            "CardProfile": card_profile
        }
    }

    # Écrire les données dans le fichier
    with open(OutputJsonLog, "w") as json_file:
        json.dump(data, json_file, indent=4)

def check_uid(filename, uid_to_check):
    # Ouvrir le fichier JSON et le lire
    with open(filename) as json_file:
        data = json.load(json_file)

    # Récupérer la liste des UID autorisés
    granted_uids = data["GrantedUID"]

    # Vérifier si l'UID donné est présent dans la liste
    if uid_to_check in granted_uids:
        return True
    else:
        return False
