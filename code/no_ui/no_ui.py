# dns.py

import network
import socket
import machine
import time

wifi_ssid = "bayar"
wifi_password = "drowssap"
static_ip = "192.168.8.180"
dns_providers_ipv4 = ["9.9.9.9", "1.1.1.1", "8.8.8.8", "94.140.14.14", "76.76.19.19", "76.76.2.0", "185.228.168.9", "208.67.222.222", "80.80.80.80"]

device_identifier = "DNS-mixer"

led_pin = machine.Pin(2, machine.Pin.OUT)

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.ifconfig((static_ip, "255.255.255.0", "192.168.8.1", "9.9.9.9"))
    sta_if.connect(wifi_ssid, wifi_password)

    while not sta_if.isconnected():
        time.sleep(1)

    blink(5, 0.3, 0.2)

def blink(num_blinks, on_duration, off_duration):
    for _ in range(num_blinks):
        led_pin.off()
        time.sleep(on_duration)
        led_pin.on()
        time.sleep(off_duration)

def handle_dns_request(data, addr):
    success = False

    for dns_provider in dns_providers_ipv4:
        dns_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dns_socket.settimeout(0.04)

        try:
            dns_socket.sendto(data, (dns_provider, 53))
            response, _ = dns_socket.recvfrom(1024)
            server_socket.sendto(response, addr)
            blink(1, 0.07, 0)  # Blink once for success
            success = True
            print("Success to resolve using DNS provider:", dns_provider)
            break
        except:
            print("Failed to resolve using DNS provider:", dns_provider)
        finally:
            dns_socket.close()

    if not success:
        blink(1, 0.2, 0)  # Blink once for failure

    return success

connect_to_wifi()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 53))

while True:
    data, addr = server_socket.recvfrom(1024)
    success = handle_dns_request(data, addr)
