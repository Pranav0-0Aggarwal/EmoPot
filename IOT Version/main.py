import time
import BlynkLib
import _thread
from faces import run
from webpage import webpage
from face_check import check, rain_check
from health import calculate_health
from sensors import temp_hum, sunlight, moisture
import socket
import network

#define BLYNK_TEMPLATE_ID "TMPL3Ii9v9td6"
#define BLYNK_TEMPLATE_NAME "EmoPot"
#define BLYNK_AUTH_TOKEN "_ZvhSjX8Z3bXwifW6-xqZO5bq3vupxMP"
BLYNK_AUTH = "_ZvhSjX8Z3bXwifW6-xqZO5bq3vupxMP"
SSID="Airel_7206010110"
PASS="air93890"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASS)


# Global variables for sensor readings
flag=False
temperature = 0
humidity = 0
moisture = 0
sunlight = 0
sensor_lock = _thread.allocate_lock()

blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('WiFi connection failed')
else:
    print('Connected')
    ip = wlan.ifconfig()[0]
    print('IP:', ip)

def read_sensors():
    global temperature, humidity, moisture, sunlight
    prev_var = ""
    counter = 0
    while True:
        with sensor_lock:
            temperature,humidity = temp_hum()
            moisture = moisture()
            sunlight = sunlight()
            if prev_var != check(temperature, moisture, sunlight, humidity) or flag:
                run("clear")
                prev_var = check(temperature, moisture, sunlight, humidity)
                print("Drawing Face")
                run(prev_var)
                flag=False
            # Send sensor data to Blynk
            blynk.virtual_write(2, temperature)  # virtual pin 1 for temperature
            blynk.virtual_write(0, moisture)    # virtual pin 2 for humidity
            blynk.virtual_write(3, sunlight)   # virtual pin 3 for pressure
            blynk.virtual_write(4, humidity)   # virtual pin 3 for pressure
            blynk.virtual_write(5, calculate_health(temperature, moisture, sunlight, humidity))   # virtual pin 3 for pressure
            blynk.run()
        time.sleep(5)  # Adjust the interval between readings if needed

def main():
    global flag
    _thread.start_new_thread(read_sensors, ())
    counter = 0
    while True:
        if counter % 10 == 0:
            with sensor_lock:
                if rain_check(temperature, humidity):
                    run("rain")
                    
                if not rain_check(temperature,humidity):
                    run("clear")
                    flag=True
        counter += 1
        time.sleep(0)  # Allow other threads to run

try:
    # Start the main thread
    main()
except KeyboardInterrupt:
    pass
finally:
    # Clean up and exit
    blynk.disconnect()


