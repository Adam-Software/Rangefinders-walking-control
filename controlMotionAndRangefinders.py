#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from Serial.serialPi import SerialU

class MotionAndRangefinders():

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
            return self._motion(sensorId, 0, 0)

    
    # if sensorId == 17 or 103
    # return [0, 0, 0, 0]
    # [sensorId, distance1, distance2, distance3]
    # if sensorId != 17 or 103 no data return
    # if isTest=True and sensorId == 17 or 103 returned example test arreay [sensorId, 10, 20, 30]
    def setMotion(self, sensorId,  speed1, speed2, isTest=False):
        
        if sensorId != 17 and sensorId != 103:
            self._motion(0, speed1, speed2)
        else:
            data = self._motion(sensorId, speed1, speed2, 255)
            
            if isTest:
                data = [sensorId, 10, 20, 30]
                return data
            else:
                return data

    # return [0, 0, 0, 0]
    # [sensorId, distance1, distance2, distance3]
    # sensorId = 17/103, left/right
    # speed1 - ??
    # speed2 - ??
    def _motion(self, sensorId, speed1, speed2, enableRangefinders=0):
        speed1 = self._speedAbs(speed1)
        speed2 = self._speedAbs(speed2)

        data = [18, sensorId, self._speedShift(speed1), self._speedMasking(speed1), self._speedShift(speed2), self._speedMasking(speed2), enableRangefinders]
        data.append(self._CRC8(data[1:]))
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
    
    #Servo utils 
    def _speedAbs(self, speed):
        if speed >= 0:
            return speed
        if speed < 0:
            return 65534 - abs(speed)
        
    #Byte utils
    def _speedShift(self, speed):
        return speed >> 8 

    #Byte utils
    def _speedMasking(self, speed):
        return speed & 0xff

    #read/write serial
    def _CRC8(self, mas):
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
