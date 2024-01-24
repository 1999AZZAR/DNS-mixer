# DNS Mixer for esp8266/esp32

Turn your esp8266/esp32 into a DNS mixer to provide dynamic DNS resolution using multiple DNS servers. This MicroPython code allows the esp8266/esp32 to act as a DNS server, forwarding DNS requests to a randomly selected DNS provider from a predefined list. Additionally, the code includes features such as LED indication for request handling, connection status, and failure conditions.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
    - [WiFi Configuration](#wifi-configuration)
    - [DNS Providers](#dns-providers)
    - [LED Pin Configuration](#led-pin-configuration)
4. [Usage](#usage)
    - [Connecting to WiFi](#connecting-to-wifi)
    - [Handling DNS Requests](#handling-dns-requests)
5. [LED Indications](#led-indications)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This MicroPython code transforms the esp8266/esp32 into a DNS mixer, allowing it to handle DNS requests from connected devices and forward them to randomly selected DNS providers. The code is designed to provide flexibility and support LED indications for debugging purposes.

## Requirements

- esp8266/esp32 device with MicroPython support. [read more..](setup/server.md)
- Network connectivity between the esp8266/esp32 and the devices making DNS requests [read more..](setup/otherdevices.md)

## Configuration

### WiFi Configuration

Adjust the WiFi settings in the code to match your network credentials.

```python
wifi_ssid = "your_wifi_ssid"
wifi_password = "your_wifi_password"
static_ip = "your_static_ip"
```

### DNS Providers

Modify the list of DNS providers to suit your preferences.

```python
dns_providers_ipv4 = ["9.9.9.9", "149.112.112.112", "1.0.0.1","94.140.14.14", "1.1.1.1", "8.8.8.8"]
```

### LED Pin Configuration

Configure the GPIO pin for the LED indicator in the code.

```python
led_pin = machine.Pin(your_led_pin_number, machine.Pin.OUT)
```

## Usage

### Connecting to WiFi

The code includes a function to connect to WiFi. Ensure the esp8266/esp32 is within range of the WiFi network.

```python
connect_to_wifi()
```

### Handling DNS Requests

The main function `handle_dns_request` is responsible for processing DNS requests, forwarding them to a randomly chosen DNS provider, and handling LED indications.

```python
handle_dns_request(data, addr)
```

## LED Indications

The code uses the onboard LED to provide indications for various events:

- Blink for 0.1 seconds on a new DNS request.
- Blink for half second on a failed DNS request.
- Blink three times fast when connected to the router.

## Troubleshooting

If you encounter issues, refer to the troubleshooting section in the code. Enable debugging prints to gain insights into the code execution.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).
