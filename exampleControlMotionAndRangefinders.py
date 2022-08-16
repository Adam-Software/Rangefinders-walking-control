import time
from controlMotionAndRangefinders import AdamMotionAndRangefinders


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

#управляем моторами и возврящаем значение 
print('Call motion with speed1 = 2000 and speed2 = 2000')
time.sleep(0.1)
motion = pp.motion(17, 2000, 2000)
print(motion)

print('Call motion with speed1 = -2000 and speed2 = -2000')
time.sleep(0.1)
motion = pp.motion(17, -2000, -2000)
print(motion)