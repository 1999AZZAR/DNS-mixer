# Setting Up esp8266/esp32 as DNS Provider

This tutorial provides step-by-step instructions on how to set up your esp8266/esp32 as a DNS provider using MicroPython. By following these steps, you'll transform your esp8266/esp32 into a DNS mixer, allowing it to handle DNS requests from connected devices and forward them to randomly selected DNS providers.

## Prerequisites

Before starting, ensure you have the following:

- An esp8266/esp32 device with MicroPython support.
- A computer with a MicroSD card reader (optional, for flashing MicroPython firmware).

## Steps

### 1. Install MicroPython Firmware

If your esp8266/esp32 doesn't have MicroPython installed, you'll need to flash the MicroPython firmware onto it. Follow these steps to do it manually or u can simply use [thonny ide](https://thonny.org/).

#### a. Download MicroPython Firmware

Visit the [MicroPython download page](https://micropython.org/download/) and download the latest esp8266/esp32 firmware.

#### b. Flash MicroPython Firmware

Use a tool like [esptool](https://github.com/espressif/esptool) to flash the MicroPython firmware onto your esp8266/esp32. Here's a sample command:

```bash
esptool.py --chip esp8266/esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firmware.bin
```

Replace `/dev/ttyUSB0` with the correct port for your esp8266/esp32 device, and `esp8266/esp3` with your actual device `ESP32` or `ESP8266`

### 2. Connect to esp8266/esp32

Use a tool like [picocom](https://github.com/npat-efault/picocom) or [minicom](https://linux.die.net/man/1/minicom) to connect to your esp8266/esp32. For example:

```bash
picocom /dev/ttyUSB0 -b 115200
```

Replace `/dev/ttyUSB0` with the correct port for your esp8266/esp32 device.

### 3. Modify Configuration

Edit the micropython file to configure your WiFi settings, DNS providers, and LED pin:

```python
wifi_ssid = "your_wifi_ssid"
wifi_password = "your_wifi_password"
static_ip = "your_static_ip"
dns_providers_ipv4 = ["9.9.9.9", "149.112.112.112", "1.0.0.1","94.140.14.14", "1.1.1.1", "8.8.8.8"]
led_pin = machine.Pin(your_led_pin_number, machine.Pin.OUT)
```

### 4. Copy Code to esp8266/esp32

Copy the DNS mixer code to your esp8266/esp32. You can use a tool like [rshell](https://github.com/dhylands/rshell) or [ampy](https://github.com/scientifichackers/ampy) for this. For example:

```bash
ampy -p /dev/ttyUSB0 put main.py
```

this will make the code to be executed on the next boot automaticaly.

**note** : dont forget to name it as `main.py` on saving it into the device.

### 5. Test DNS Resolution

Now that your esp8266/esp32 is acting as a DNS provider, you can test DNS resolution from devices connected to the same network. Configure the DNS settings on your devices to use the static IP address you set for the esp8266/esp32 (`your_static_ip`).

### 6. LED Indications

Observe the LED on the esp8266/esp32 for indications:

- Blink for 0.1 seconds on a new DNS request.
- Blink for half second on a failed DNS request.
- Blink three times fast when connected to the router.

Congratulations! You have successfully set up your esp8266/esp32 as a DNS provider using MicroPython. Feel free to explore the code and customize it further to suit your needs.
