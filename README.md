# DNS Mixer

Welcome to DNS-mixer! This project handles DNS requests and forwards them to multiple DNS providers, ensuring reliability and redundancy in DNS resolution.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
    - [WiFi Configuration](#wifi-configuration)
    - [DNS Providers](#dns-providers)
4. [Usage](#usage)
    - [Connecting to WiFi](#connecting-to-wifi)
    - [Handling DNS Requests](#handling-dns-requests)
5. [Troubleshooting](#troubleshooting)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

DNS-mixer is a Python-based DNS forwarding tool designed to provide flexibility and resilience by dynamically switching between multiple DNS providers. This project aims to offer a reliable DNS resolution mechanism.

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

## Troubleshooting

If you encounter issues, refer to the troubleshooting section in the code. Enable debugging prints to gain insights into the code execution.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).
