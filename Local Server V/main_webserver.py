import uasyncio as asyncio
import time
from faces import run
from webpage import webpage
from face_check import check, rain_check
from health import calculate_health
from sensors import temp_hum, sunlight, moisture
import socket
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Airel_7206010110", "air93890")

# Global variables for sensor readings
temperature = 0
humidity = 0
moisture = 0
sunlight = 0

# Function to read sensor values and determine appropriate face
async def read_sensors():
    global temperature, humidity, moisture, sunlight
    prev_var = ""
    counter = 3600
    while True:
        print("Hi")
        temperature = 25.0
        humidity = 60.0
        moisture = 50.0
        sunlight = 50.0
        
        #if rain_check(temperature, humidity) and counter // 3600 == 1:
            #counter = 0
            #run("rain")
        #counter += 1
        

        if prev_var != check(temperature, moisture, sunlight, humidity):
            run("clear")
        prev_var = check(temperature, moisture, sunlight, humidity)
        run(check(temperature, moisture, sunlight, humidity))
        await asyncio.sleep(1)  # Adjust the interval between readings if needed

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
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip = wlan.ifconfig()[0]
    print('IP: ', ip)

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(5)
print('listening on', addr)

# Function to handle client connections
def handle_client(client_socket):
    # Receive the client's request
    request = client_socket.recv(1024).decode()

    # Check if a user is accessing the webpage
    if "GET /" in request:
        
        # Call the webpage function from webpage.py and pass sensor values as arguments
        html_string = webpage(
            "EmoPot",
            temperature,
            moisture,
            sunlight,
            humidity,
            calculate_health(temperature, moisture, sunlight, humidity),
        )  # Replace with additional required variables

        # Send HTTP headers and the HTML content
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "Content-Length: {}\r\n".format(len(html_string))
        response += "\r\n"
        response += html_string

        # Send the response to the client
        client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()

# Start a coroutine to handle client connections
async def start_server():
    while True:
        print("bye")
        # Accept a client connection
        client_socket, client_address = server.accept()

        # Start a task to handle the client connection
        handle_client(client_socket)

        # Delay to avoid overwhelming the system
        await asyncio.sleep(1)  # Adjust the interval between checks if needed

# Create an event loop and schedule the tasks


loop = asyncio.get_event_loop()
loop.create_task(read_sensors())
loop.create_task(start_server())

try:
    # Run the event loop
    loop.run_forever()
except KeyboardInterrupt:
    # Close the server and release the bind port
    server.close()
    loop.close()

