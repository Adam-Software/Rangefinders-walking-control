import time
from motionAndRangefinders import MotionAndRangefinders


pp=AdamMotionAndRangefinders()

#имитация возврата резульатов, имитирующих реальные данные [103, 10, 20, 30]
left_sensor = pp.getDistance(17, True)
time.sleep(0.1)
print('Get distance with fake return value')
print(left_sensor)

#возврат реальных результатов, если дальномер не подключен то [0, 0, 0, 0]
left_sensor = pp.getDistance(17)
time.sleep(0.1)
print('Get distance with real return value')
print(left_sensor)

#имитация возврата резульатов, имитирующих реальные данные [103, 10, 20, 30]
right_sensor = pp.getDistance(103, True)
time.sleep(0.1)
print('Get distance with fake return value')
print(right_sensor)

#возврат реальных результатов, если дальномер не подключен то [0, 0, 0, 0]
right_sensor = pp.getDistance(103)
time.sleep(0.1)
print('Get distance with real return value')
print(right_sensor)

#едем вперед и не возврящаем значение 
print('Call motion with speed1 = 2000 and speed2 = 2000 no return value')
time.sleep(0.1)
motion = pp.setMotion(0, 2000, 2000)
print(motion)

#едем назад и не возврящаем значение 
print('Call motion with speed1 = -2000 and speed2 = -2000 no return value')
time.sleep(0.1)
motion = pp.setMotion(0, -2000, -2000)
print(motion)

#едем вперед и возврящаем реальные значение с сенсора 17 
print('Call motion with sensor 17 speed1 = 2000 and speed2 = 2000 and return rangefinders data ([0, 0, 0, 0] if uart disconect)') 
time.sleep(0.1)
motion = pp.setMotion(17, 2000, 2000)
print(motion)

#едем вперед и возврящаем реальные значение с сенсора 103
print('Call motion with sensor 103 speed1 = 2000 and speed2 = 2000 and return rangefinders data ([0, 0, 0, 0] if uart disconect)') 
time.sleep(0.1)
motion = pp.setMotion(103, 2000, 2000)
print(motion)

#едем вперед и возврящаем тестовые значения 
print('Call motion with sensor 17  speed1 = 2000 and speed2 = 2000 and return rangefinders test array [17, 10, 20, 30]') 
time.sleep(0.1)
motion = pp.setMotion(17, 2000, 2000, True)
print(motion)

#едем вперед и возврящаем тестовые значения 
print('Call motion with sensor 103 speed1 = 2000 and speed2 = 2000 and return rangefinders test array [103, 10, 20, 30]') 
time.sleep(0.1)
motion = pp.setMotion(103, 2000, 2000, True)
print(motion)

#едем вперед и указываем неверный сенсор
print('Call motion with sensor 160 speed1 = 2000 and speed2 = 2000 and return None') 
time.sleep(0.1)
motion = pp.setMotion(160, 2000, 2000, True)
print(motion)
