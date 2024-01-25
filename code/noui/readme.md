# DNS-mixer

## Introduction

DNS-mixer is a Python-based DNS forwarding tool designed to provide flexibility and resilience by dynamically switching between multiple DNS providers. This project aims to offer a reliable DNS resolution mechanism with LED indications for various events.

## Requirements

Ensure you have the following prerequisites before using DNS-mixer:

- Microcontroller board (e.g., ESP8266)
- MicroPython environment
- Network connectivity for DNS forwarding
- LEDs for visual indications

## Configuration

### WiFi Configuration

Adjust the WiFi settings in the code to match your network:

```python
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"
STATIC_IP = "your_static_ip"
```

### DNS Providers

Modify the list of DNS providers to suit your preferences:

```python
DNS_PROVIDERS_IPV4 = ["9.9.9.9", "1.1.1.1", "8.8.8.8", "94.140.14.14", "76.76.19.19", "76.76.2.0", "185.228.168.9",
                     "208.67.222.222", "80.80.80.80"]
```

### LED Pin Configuration

Customize the LED pin based on your hardware setup:

```python
LED_PIN = machine.Pin(your_led_pin, machine.Pin.OUT)
```

## Usage

### Connecting to WiFi

Ensure a stable connection to WiFi by configuring the WiFi settings and running the script on your microcontroller.

### Handling DNS Requests

The script automatically handles DNS requests by forwarding them to multiple DNS providers. LED indications provide visual feedback on the status of each request.

## LED Indications

- Blink for 0.05 seconds: New DNS request received
- Blink for 0.07 seconds: Successful DNS resolution
- Blink for 0.5 seconds: Failure to forward DNS request

## Troubleshooting

If you encounter issues, check the following:

- WiFi configuration (SSID, password, static IP)
- DNS provider availability
- LED pin configuration

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests on the project repository.

## License

This project is licensed under the [MIT License](LICENSE).
