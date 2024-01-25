# DNS-mixer

## Introduction

Welcome to DNS-mixer! This project handles DNS requests and forwards them to multiple DNS providers, ensuring reliability and redundancy in DNS resolution.

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

## Usage

### Connecting to WiFi

The `connect_to_wifi` function connects DNS-mixer to your WiFi network. Ensure your WiFi credentials are correctly set in the configuration.

### Handling DNS Requests

The `handle_dns_request` function processes incoming DNS requests, forwarding them to multiple DNS providers for resolution. LED indicators provide feedback on the status of the DNS resolution.

## Contributing

Feel free to contribute to the project by providing feedback, reporting issues, or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
