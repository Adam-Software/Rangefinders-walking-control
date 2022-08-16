#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from Serial.serialPi import SerialU

class AdamMotionAndRangefinders():

    def __init__(self):
        super().__init__()
        self.ser = SerialU('/dev/ttyAMA0', 115200)
        self.sensors=[0, 0, 0, 0]

    # return [0, 0, 0, 0]
    # [sensorId, distance1, distance2, distance3]
    # sensorId = 17/103, left/right
    def getDistance(self, sensorId, isTest=False):
        if isTest:
            return [sensorId, 10, 20, 30]
        else:
            return self.motion(sensorId, 0, 0)

    # return [0, 0, 0, 0]
    # [sensorId, distance1, distance2, distance3]
    # sensorId = 17/103, left/right
    # speed1 - ??
    # speed2 - ??
    def motion(self, sensorId, speed1, speed2):
        speed1 = self.speedAbs(speed1)
        speed2 = self.speedAbs(speed2)

        data = [18, sensorId, self.speedShift(speed1), self.speedMasking(speed1), self.speedShift(speed2), self.speedMasking(speed2), 255]
        data.append(self.CRC8(data[1:]))
        data.append(36)
        self.ser.write(data, len(data))
        time.sleep(0.02)

        if  self.ser.avail():
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
    
    #Utils

    def speedAbs(self, speed):
        if speed >= 0:
            return speed
        if speed < 0:
            return 65534 - abs(speed)
        
    
    def speedShift(self, speed):
        return speed >> 8 

    def speedMasking(self, speed):
        return speed & 0xff

    #read/write serial

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