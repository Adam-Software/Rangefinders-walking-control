#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from Serial.serialPi import SerialU

class AdamRangefinders():

def __init__(self):
    super().__init__()
    self.ser = SerialU('/dev/ttyAMA0', 115200)
    self.sensors=[0, 0, 0, 0]

def CRC8(self, mas):
    st_byt = 0
    crc = 0
    while st_byt < len(mas):
       dat = mas[st_byt]
       for i in range(8):
           fb = crc ^ dat
           fb &= 1
           crc >>= 1
           dat >>= 1
           if fb == 1:
               crc ^= 0x8c
        st_byt += 1
    return crc


def distance(self, sensorId):
    data = [18, sensorId, 0, 0, 0, 0, 255]
    data.append(self.CRC8(data[1:]))
    data.append(36)
    self.ser.write(data, len(data))
    time.sleep(0.02)

    if self.ser.avail():
        text = self.ser.readByte('$', 100, 100)
        time.sleep(0.02)
        text=text.decode('utf-8')
        t=''
        t=text[:text.find('$')]
        t=t.split(',')

        dataSens=[]

        try:
            for n in t:
                dataSens.append(int(n))
            except:
                pass

        if len(dataSens)>1:
            if dataSens[0]==sensorId:
                self.sensors=dataSens

        return self.sensors

def getDistance(self, sensorId, isTest=False):
    if isTest:
        return [sensorId, 10, 20, 30]
    else:
        return self.distance(sensorId)