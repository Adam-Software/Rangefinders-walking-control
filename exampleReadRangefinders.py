import time
from readRangefinders import AdamRangefinders


pp=AdamRangefinders()

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
