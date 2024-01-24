# MicroPython DNS Mixer for ESP32 and ESP8266

## Introduction

The MicroPython DNS Mixer is a script tailored for ESP32 and ESP8266 devices, crafted to handle DNS requests by sending them to multiple DNS providers and utilizing the first one that responds. This script is designed to enhance DNS resolution reliability by leveraging the redundancy of multiple DNS servers.

## Configuration

Before deploying the MicroPython DNS Mixer on your ESP32 or ESP8266 device, configure the following parameters in the script:

- `wifi_ssid`: The SSID of the WiFi network.
- `wifi_password`: The password for the WiFi network.
- `static_ip`: The static IP address assigned to the device.
- `dns_providers_ipv4`: A list of IPv4 addresses of DNS providers to be used.
- `device_identifier`: A unique identifier for the device.
- `led_pin`: GPIO pin for the LED indicator.

## Functionality

The MicroPython DNS Mixer operates by iteratively going through each DNS provider and using the first one that responds to a DNS request. The LED indicator provides visual feedback on the status of DNS requests, blinking for short durations on each request and longer durations on failures.

## Usage

1. Flash the MicroPython firmware onto your ESP32 or ESP8266 device.
2. Copy the MicroPython DNS Mixer script onto the device.
3. Modify the script with your WiFi and DNS configuration.
4. Run the script on the ESP32 or ESP8266 device.

## Dependencies

- MicroPython
- ssd1306 library (optional, for OLED display)

## Differentiation

### [random](use_random.py)

- Chooses a DNS provider randomly on each DNS request.
- Utilizes `urandom` to generate a random index for selecting a DNS provider.
- LED blinks for a short duration on each DNS request.

### [iteration](use_iteration.py)

- Iterates through each DNS provider and uses the first one that responds.
- LED blinks for a short duration on each DNS request and a longer duration on failure.

## License

This MicroPython DNS Mixer project is licensed under the [MIT License](../../LICENSE).
