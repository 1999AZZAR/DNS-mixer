import network
import socket
import machine
import time
from microWebSrv import MicroWebSrv
from machine import I2C, Pin
import ssd1306

# Constants
WIFI_SSID = "bayar"
WIFI_PASSWORD = "drowssap"
STATIC_IP = "192.168.8.180"
DNS_PROVIDERS_IPV4 = ["9.9.9.9", "1.1.1.1", "8.8.8.8", "94.140.14.14", "76.76.19.19", "76.76.2.0", "185.228.168.9",
                     "208.67.222.222", "80.80.80.80"]

# Unique device identifier
DEVICE_IDENTIFIER = "DNS-mixer"

# Pin configuration
LED = machine.Pin(2, machine.Pin.OUT)

# OLED display configuration
i2c = I2C(sda=Pin(4), scl=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Counters
TOTAL_REQUESTS = 0
TOTAL_SUCCESS = 0
TOTAL_REJECT = 0

# Function to perform blinking
def blink(num_blinks, on_duration, off_duration):
    for _ in range(num_blinks):
        LED.value(1)
        time.sleep(on_duration)
        LED.value(0)
        time.sleep(off_duration)

# Function to connect to WiFi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.ifconfig((STATIC_IP, "255.255.255.0", "192.168.8.1", "8.8.8.8"))
    sta_if.connect(WIFI_SSID, WIFI_PASSWORD)

    while not sta_if.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi")
    blink(5, 0.2, 0.3)

# Function to handle DNS requests
def handle_dns_request(data, addr):
    print("Received DNS request from:", addr)
    blink(1, 0.05, 0)

    success = False

    for dns_provider in DNS_PROVIDERS_IPV4:
        print("Trying DNS provider:", dns_provider)

        dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_socket.settimeout(0.03)

        try:
            dns_socket.sendto(data, (dns_provider, 53))
            response, _ = dns_socket.recvfrom(1024)
            server_socket.sendto(response, addr)
            blink(1, 0.02, 0)
            success = True
            break
        except:
            print("Failed to resolve using DNS provider:", dns_provider)
        finally:
            dns_socket.close()

    if not success:
        blink(1, 0.5, 0)
        print("Failed to forward DNS request")

    return success

# Initialize MicroWebSrv
mws = MicroWebSrv(webPath='/www')

# Function to handle HTTP requests
def http_handler(httpClient, httpResponse):
    content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>DNS Mixer Stats</title>
        </head>
        <body>
            <h1>DNS Mixer Stats</h1>
            <p>Device Identifier: {0}</p>
            <p>IP: {1}</p>
            <p>Total Requests: {2}</p>
            <p>Success: {3}</p>
            <p>Reject: {4}</p>
        </body>
    </html>
    """.format(DEVICE_IDENTIFIER, STATIC_IP, TOTAL_REQUESTS, TOTAL_SUCCESS, TOTAL_REJECT)

    httpResponse.WriteResponseOk(headers=None,
                                 contentType="text/html",
                                 contentCharset="UTF-8",
                                 content=content)

# Start the MicroWebSrv
mws.Start()

# Connect to WiFi
connect_to_wifi()

# Create a UDP socket for DNS
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 53))

# Main loop to handle DNS requests
while True:
    data, addr = server_socket.recvfrom(1024)
    success = handle_dns_request(data, addr)

    TOTAL_REQUESTS += 1
    if success:
        TOTAL_SUCCESS += 1
    else:
        TOTAL_REJECT += 1

    oled.fill(0)
    oled.text(DEVICE_IDENTIFIER, 30, 0, 1)
    oled.text("IP:" + STATIC_IP, 0, 12, 1)
    oled.text("Total: " + str(TOTAL_REQUESTS), 0, 24, 1)
    oled.text("Success: " + str(TOTAL_SUCCESS), 0, 36, 1)
    oled.text("Reject: " + str(TOTAL_REJECT), 0, 48, 1)
    oled.show()

    time.sleep(0.3)
