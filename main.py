import network
import socket
import machine
import time
import urandom

# Configuration
wifi_ssid = "your_wifi_ssid"
wifi_password = "your_wifi_password"
static_ip = "your_static_ip"
dns_providers_ipv4 = ["9.9.9.9", "149.112.112.112", "1.0.0.1","94.140.14.14", "1.1.1.1", "8.8.8.8"]

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

    # Blink LED for 0.1 seconds on new request
    led_pin.on()
    time.sleep(0.1)
    led_pin.off()

    # Choose a DNS provider randomly
    dns_provider = dns_providers_ipv4[urandom.getrandbits(2) % len(dns_providers_ipv4)]
    print("Using DNS provider:", dns_provider)

    # Create a UDP socket to forward the DNS request
    dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dns_socket.settimeout(1)

    try:
        dns_socket.sendto(data, (dns_provider, 53))
        response, _ = dns_socket.recvfrom(1024)
        # Forward the DNS response to the original requester
        server_socket.sendto(response, addr)
    except:
        # Blink LED for 1 second on failure
        led_pin.on()
        time.sleep(0.5)
        led_pin.off()
        print("Failed to forward DNS request")

    dns_socket.close()

# Connect to WiFi
connect_to_wifi()

# Create a UDP socket for DNS
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 53))

# Blink LED 3 times fast on connected to router
for _ in range(3):
    led_pin.on()
    time.sleep(0.2)
    led_pin.off()
    time.sleep(0.2)

print("Connected to router")

# Main loop to handle DNS requests
while True:
    data, addr = server_socket.recvfrom(1024)
    handle_dns_request(data, addr)
