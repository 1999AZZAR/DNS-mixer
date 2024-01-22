# Setting Up ESP32 as DNS Provider

This tutorial provides step-by-step instructions on how to set up your ESP32 as a DNS provider using MicroPython. By following these steps, you'll transform your ESP32 into a DNS mixer, allowing it to handle DNS requests from connected devices and forward them to randomly selected DNS providers.

## Prerequisites

Before starting, ensure you have the following:

- An ESP32 device with MicroPython support.
- A computer with a MicroSD card reader (optional, for flashing MicroPython firmware).

## Steps

### 1. Install MicroPython Firmware

If your ESP32 doesn't have MicroPython installed, you'll need to flash the MicroPython firmware onto it. Follow these steps:

#### a. Download MicroPython Firmware

Visit the [MicroPython download page](https://micropython.org/download/esp32/) and download the latest ESP32 firmware.

#### b. Flash MicroPython Firmware

Use a tool like [esptool](https://github.com/espressif/esptool) to flash the MicroPython firmware onto your ESP32. Here's a sample command:

```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-firmware.bin
```

Replace `/dev/ttyUSB0` with the correct port for your ESP32 device.

### 2. Connect to ESP32

Use a tool like [picocom](https://github.com/npat-efault/picocom) or [minicom](https://linux.die.net/man/1/minicom) to connect to your ESP32. For example:

```bash
picocom /dev/ttyUSB0 -b 115200
```

Replace `/dev/ttyUSB0` with the correct port for your ESP32 device.

### 3. Copy Code to ESP32

Copy the DNS mixer code to your ESP32. You can use a tool like [rshell](https://github.com/dhylands/rshell) or [ampy](https://github.com/scientifichackers/ampy) for this. For example:

```bash
ampy -p /dev/ttyUSB0 put esp32_dns_mixer.py
```

### 4. Modify Configuration

Edit the `esp32_dns_mixer.py` file to configure your WiFi settings, DNS providers, and LED pin:

```python
wifi_ssid = "your_wifi_ssid"
wifi_password = "your_wifi_password"
static_ip = "your_static_ip"
dns_providers_ipv4 = ["9.9.9.9", "149.112.112.112", "1.0.0.1","94.140.14.14", "1.1.1.1", "8.8.8.8"]
led_pin = machine.Pin(your_led_pin_number, machine.Pin.OUT)
```

### 5. Connect ESP32 to WiFi

Run the following commands on the ESP32 to connect it to your WiFi network:

```python
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.ifconfig((static_ip, "255.255.255.0", "192.168.8.1", "8.8.8.8"))
sta_if.connect(wifi_ssid, wifi_password)
```

### 6. Run DNS Mixer

Run the following commands on the ESP32 to start the DNS mixer:

```python
import esp32_dns_mixer
esp32_dns_mixer.run_dns_mixer()
```

### 7. Test DNS Resolution

Now that your ESP32 is acting as a DNS provider, you can test DNS resolution from devices connected to the same network. Configure the DNS settings on your devices to use the static IP address you set for the ESP32 (`your_static_ip`).

### 8. LED Indications

Observe the LED on the ESP32 for indications:

- Blink for 0.1 seconds on a new DNS request.
- Blink for half second on a failed DNS request.
- Blink three times fast when connected to the router.

Congratulations! You have successfully set up your ESP32 as a DNS provider using MicroPython. Feel free to explore the code and customize it further to suit your needs.
