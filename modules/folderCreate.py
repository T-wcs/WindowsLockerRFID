#!/usr/env/python3
#coding:utf-8

import os

currentUser = os.environ["USERNAME"]

def create_folder():
    folder_path = "C:\\Users\\{}\\AppData\\Local\\Programs\\WinLockerRFID".format(currentUser)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass
