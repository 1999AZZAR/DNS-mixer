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
  - [OLED](#oled)
  - [WEB](#web)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to DNS-mixer! This project is designed to handle DNS requests and forward them to multiple DNS providers, providing reliability and redundancy in DNS resolution.

## Requirements

To use DNS-mixer, you need the following:

- Microcontroller with MicroPython support
- WiFi network credentials (SSID and Password)
- DNS providers' IP addresses

## Configuration

### WiFi Configuration

Update the following constants in the code to match your WiFi network:

```python
WIFI_SSID = "your_ssid"
WIFI_PASSWORD = "your_password"
STATIC_IP = "your_static_ip"
```

### DNS Providers

Adjust the list of DNS providers' IPv4 addresses as needed:

```python
DNS_PROVIDERS_IPV4 = ["9.9.9.9", "1.1.1.1", "8.8.8.8", ...]
```

### Hardware Pin Configuration

Configure the hardware pins for LED, I2C, and other peripherals if necessary:

```python
LED_PIN = machine.Pin(2, machine.Pin.OUT)
i2c = I2C(sda=Pin(4), scl=Pin(5))
```

## Usage

### Connecting to WiFi

The `connect_to_wifi` function connects DNS-mixer to your WiFi network. Ensure your WiFi credentials are correctly set in the configuration.

### Handling DNS Requests

The `handle_dns_request` function processes incoming DNS requests, forwarding them to multiple DNS providers for resolution. LED indicators provide feedback on the status of the DNS resolution.

## Indications

### LED

The LED blinks to indicate different states:

- Short blink: New DNS request received
- Short double blink: Successful DNS resolution
- Long blink: Failed to forward DNS request

### OLED

An OLED display provides real-time stats, including device identifier, IP address, total requests, successful resolutions, and rejections.

### WEB

A simple web server displays DNS Mixer statistics. Access it by navigating to the device's IP address in a web browser.

## Troubleshooting

If you encounter issues, refer to the troubleshooting section in the code and check the LED and OLED indicators for additional feedback.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests on the project repository.

## License

This project is licensed under the [MIT License](LICENSE).
