from gpiozero import CPUTemperature
import datetime
import itertools
import time

# dummy clase sensor que simula datos de un sensor
class Sensor():
    def __iter__(self):
        return self

    def __next__(self):
        return CPUTemperature().temperature

sensor = Sensor()
# Generamos un iterable para la fecha
timestamps = iter(datetime.datetime.now, None)

# Podemos generarnos un bucle con nuestros dos iterables. Mediante zip generamos un iterable conjunto
for stamp,sensor_value in itertools.islice(zip(timestamps, sensor), 10):
    print(stamp, sensor_value)
    time.sleep(1)
