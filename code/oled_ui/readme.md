# DNS-mixer Readme

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
   - [WiFi Configuration](#wifi-configuration)
   - [DNS Providers](#dns-providers)
   - [Hardware Pin Configuration](#hardware-pin-configuration)
4. [Usage](#usage)
   - [Connecting to WiFi](#connecting-to-wifi)
   - [Handling DNS Requests](#handling-dns-requests)
5. [Indications](#indications)
   - [LED](#led)
   - [OLED](#oled)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

Welcome to DNS-mixer, a Python project designed to enhance DNS request handling through the mixing of various DNS providers. This project focuses on efficiently forwarding DNS requests to multiple providers, increasing reliability and reducing latency.

## Requirements

To use DNS-mixer, ensure you have the following components:

- Microcontroller with Python support
- OLED display (SSD1306)
- LED indicator
- WiFi connectivity

## Configuration

### WiFi Configuration

Adjust the WiFi settings by modifying the following constants in the code:

```python
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"
STATIC_IP = "your_static_ip_address"
```

### DNS Providers

Customize the list of DNS providers to be used. The default list includes some popular providers:

```python
DNS_PROVIDERS_IPV4 = ["9.9.9.9", "1.1.1.1", "8.8.8.8", "94.140.14.14", "76.76.19.19", "76.76.2.0", "185.228.168.9",
                     "208.67.222.222", "80.80.80.80"]
```

### Hardware Pin Configuration

Adjust hardware pin configurations according to your setup:

```python
LED_PIN = machine.Pin(2, machine.Pin.OUT)
```

## Usage

### Connecting to WiFi

Ensure your device is connected to WiFi by invoking the `connect_to_wifi()` function:

```python
connect_to_wifi()
```

### Handling DNS Requests

The main functionality of DNS-mixer revolves around forwarding DNS requests to multiple providers. The code handles this automatically in the main loop.

---

## Indications

### LED

- The LED blinks briefly (0.05 seconds) on receiving a new DNS request.
- On successful resolution, the LED blinks for 0.07 seconds.
- If DNS resolution fails, the LED blinks for half a second.

### OLED

The OLED display provides real-time information about the DNS-mixer's performance, including total requests, successful resolutions, and rejections.

---

## Troubleshooting

For any issues or unexpected behavior, refer to the troubleshooting section in the [Wiki](link-to-wiki).

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests on the project repository.

## License

This project is licensed under the [MIT License](LICENSE).
