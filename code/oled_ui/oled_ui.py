import network
import socket
import machine
import time
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

    for _ in range(5):
        LED.value(1)
        time.sleep(0.2)
        LED.value(0)
        time.sleep(0.3)

# Function to handle DNS requests
def handle_dns_request(data, addr):
    print("Received DNS request from:", addr)

    # Blink LED for 0.05 seconds on new request
    LED.value(1)
    time.sleep(0.05)
    LED.value(0)

    success = False

    # Iterate through each DNS provider and try to resolve using the first one that responds
    for dns_provider in DNS_PROVIDERS_IPV4:
        print("Trying DNS provider:", dns_provider)

        # Create a UDP socket to forward the DNS request
        dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_socket.settimeout(0.03)

        try:
            dns_socket.sendto(data, (dns_provider, 53))
            response, _ = dns_socket.recvfrom(1024)
            # Forward the DNS response to the original requester
            server_socket.sendto(response, addr)
            # Blink LED for 0.02 second on success
            LED.value(1)
            time.sleep(0.02)
            LED.value(0)
            success = True
            break
        except:
            print("Failed to resolve using DNS provider:", dns_provider)
        finally:
            dns_socket.close()

    if not success:
        # Blink LED for half second on failure
        LED.value(1)
        time.sleep(0.5)
        LED.value(0)
        print("Failed to forward DNS request")

    return success

# Connect to WiFi
connect_to_wifi()

# Create a UDP socket for DNS
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 53))

# Initialize the OLED display
i2c = I2C(sda=Pin(4), scl=Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize counters
total_requests = 0
total_success = 0
total_reject = 0

# Main loop to handle DNS requests
while True:
    data, addr = server_socket.recvfrom(1024)
    success = handle_dns_request(data, addr)

    # Update counters
    total_requests += 1
    if success:
        total_success += 1
    else:
        total_reject += 1

    # Update OLED display with counters and device identifier
    oled.fill(0)
    oled.text(DEVICE_IDENTIFIER, 30, 0, 1)
    oled.text("IP:" + STATIC_IP, 0, 12, 1)
    oled.text("Total: " + str(total_requests), 0, 24, 1)
    oled.text("Success: " + str(total_success), 0, 36, 1)
    oled.text("Reject: " + str(total_reject), 0, 48, 1)
    oled.show()

    # Sleep for a short duration to handle requests
    time.sleep(0.03)

