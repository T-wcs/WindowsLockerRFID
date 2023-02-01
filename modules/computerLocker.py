#!/usr/env/python3
#coding:utf-8

import ctypes

def lock_computer():
    ctypes.windll.user32.LockWorkStation()
