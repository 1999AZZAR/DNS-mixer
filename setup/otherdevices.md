# Setting Up DNS on Other Devices

## 1. Locate DNS Settings

- **Windows:**
  1. Open the "Control Panel."
  2. Navigate to "Network and Sharing Center."
  3. Click on "Change adapter settings."
  4. Right-click on the active network connection and select "Properties."
  5. Choose "Internet Protocol Version 4 (TCP/IPv4)" and click on "Properties."

- **macOS:**
  1. Open "System Preferences."
  2. Select "Network."
  3. Choose the active network connection.
  4. Click on "Advanced."
  5. Go to the "DNS" tab.

- **Linux:**
  1. Open the terminal.
  2. Edit the network configuration file or use a network manager tool.
  3. Locate and edit the DNS configuration.

## 2. Configure DNS Settings

- **For Windows:**
  - Select "Use the following DNS server addresses."
  - Set the "Preferred DNS server" to the static IP address of your ESP32 (e.g., `192.168.8.180`).

- **For macOS:**
  - Click on the "+" button under the "DNS Servers" section.
  - Add the static IP address of your ESP32 (e.g., `192.168.8.180`).

- **For Linux:**
  - Edit the network configuration file (e.g., `/etc/network/interfaces` or `/etc/resolv.conf`).
  - Add or modify the `nameserver` line to include the static IP address of your ESP32.

## 3. Save and Apply Changes

- **For Windows:**
  - Click "OK" to save the changes.

- **For macOS:**
  - Click "OK" to save changes in the advanced settings.
  - Click "Apply" to apply changes in the main network settings.

- **For Linux:**
  - Save the changes to the configuration file.
  - Restart the network service or reboot the system.

## 4. Verify DNS Configuration

- Open a command prompt or terminal on the device.
- Use the `nslookup` command to check DNS resolution:

  ```bash
  nslookup example.com
  ```

  Replace `example.com` with a domain you want to look up.

If the configuration is correct, your device should now use the ESP32 as the DNS provider for DNS resolution. You can repeat these steps on other devices in the network that you want to use the ESP32 as the DNS server.
