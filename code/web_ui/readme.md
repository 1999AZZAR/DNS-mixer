# DNS-mixer

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Configuration](#configuration)
  - [WiFi Configuration](#wifi-configuration)
  - [DNS Providers](#dns-providers)
  - [Hardware Pin Configuration](#hardware-pin-configuration)
- [Usage](#usage)
  - [Connecting to WiFi](#connecting-to-wifi)
  - [Handling DNS Requests](#handling-dns-requests)
- [Indications](#indications)
  - [LED](#led)
  - [WEB](#web)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

DNS-mixer is a Python project designed to act as a DNS forwarder. It intercepts DNS requests, forwards them to multiple DNS providers in parallel, and returns the first successful response to the original requester. This project also includes a web server for displaying device statistics.

## Requirements

- MicroPython
- microWebSrv library

## Configuration

### WiFi Configuration

Edit the following constants in the code to configure WiFi settings:

```python
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"
STATIC_IP = "your_static_ip_address"
```

### DNS Providers

Edit the list of DNS providers to be used:

```python
DNS_PROVIDERS_IPV4 = ["9.9.9.9", "1.1.1.1", "8.8.8.8", "94.140.14.14", "76.76.19.19", "76.76.2.0", "185.228.168.9",
                     "208.67.222.222", "80.80.80.80"]
```

### Hardware Pin Configuration

Configure the hardware pins used by the project:

```python
LED_PIN = machine.Pin(2, machine.Pin.OUT)
```

## Usage

### Connecting to WiFi

The device automatically connects to the configured WiFi network on startup. Make sure to provide the correct WiFi credentials in the configuration.

### Handling DNS Requests

DNS requests are handled automatically. The device intercepts DNS requests, forwards them to the configured DNS providers, and returns the first successful response.

## Indications

### LED

The device uses an LED to indicate various states:
- Blink for 0.05 seconds on receiving a new DNS request.
- Blink for 0.07 seconds on successfully forwarding a DNS request.
- Blink for 0.5 seconds on failing to forward a DNS request.

### WEB

Device statistics, including device identifier, IP address, total requests, successful requests, and rejected requests, are available through a web interface.

## Troubleshooting

If you encounter issues, refer to the LED indications and check the web interface for device statistics. Ensure that the WiFi configuration is correct.

## Contributing

Contributions are welcome! Please follow standard contribution guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
