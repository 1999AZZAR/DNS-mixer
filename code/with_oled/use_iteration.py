import network
import socket
import machine
import time
from machine import I2C, Pin
import ssd1306

# Configuration
wifi_ssid = "your_wifi_ssid"
wifi_password = "your_wifi_password"
static_ip = "your_static_ip"
dns_providers_ipv4 = ["9.9.9.9", "149.112.112.112", "1.0.0.1", "94.140.14.14", "1.1.1.1", "8.8.8.8"]

# Unique device identifier
device_identifier = "DNS-mixer"

# Pin configuration for LED
led_pin = machine.Pin(2, machine.Pin.OUT)

# Function to connect to WiFi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.ifconfig((static_ip, "255.255.255.0", "192.168.8.1", "8.8.8.8"))
    sta_if.connect(wifi_ssid, wifi_password)

    while not sta_if.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)

    print("Connected to WiFi")

# Function to handle DNS requests
def handle_dns_request(data, addr):
    print("Received DNS request from:", addr)

    # Blink LED for 0.05 seconds on new request
    led_pin.on()
    time.sleep(0.05)
    led_pin.off()

    success = False

    # Iterate through each DNS provider and try to resolve using the first one that responds
    for dns_provider in dns_providers_ipv4:
        print("Trying DNS provider:", dns_provider)

        # Create a UDP socket to forward the DNS request
        dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_socket.settimeout(0.03)

        try:
            dns_socket.sendto(data, (dns_provider, 53))
            response, _ = dns_socket.recvfrom(1024)
            # Forward the DNS response to the original requester
            server_socket.sendto(response, addr)
            # Blink LED for 0.07 second on success
            led_pin.on()
            time.sleep(0.07)
            led_pin.off()
            success = True
            break
        except:
            print("Failed to resolve using DNS provider:", dns_provider)
        finally:
            dns_socket.close()

    if not success:
        # Blink LED for half second on failure
        led_pin.on()
        time.sleep(0.5)
        led_pin.off()
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
    oled.text(device_identifier, 30, 0, 1)
    oled.text("IP:" + static_ip, 0, 12, 1)
    oled.text("Total: " + str(total_requests), 0, 24, 1)
    oled.text("Success: " + str(total_success), 0, 36, 1)
    oled.text("Reject: " + str(total_reject), 0, 48, 1)
    oled.show()
