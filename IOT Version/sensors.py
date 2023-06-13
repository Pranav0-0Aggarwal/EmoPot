
from machine import Pin, I2C, ADC
import time
from dht import DHT11, InvalidChecksum

#Read sensor data

# temperature and humidity sensor
def temp_hum():
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    return t, h

#Sunlight sensor
def sunlight():
    ldr = Pin(14, Pin.IN, Pin.PULL_DOWN)
    data=ldr.value()
    return data

#moisture sensor
def moisture():
    soil = ADC(Pin(26)) # Soil moisture PIN reference
    min_moisture=19200
    max_moisture=49300
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture) 
    # print values
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    return moisture


