# Packet Sniffer

A simple packet sniffer built using the Scapy library in Python.

## Description

This packet sniffer captures network packets and displays relevant information about them, such as the protocol, source and destination IP addresses, geo-locations, source and destination ports, TCP flags, and the payload (if available). It is especially useful for monitoring and analyzing HTTP traffic.

## Requirements

- Python 3.x
- Scapy library
- ipwhois library (for geolocation feature)

## Installation

1. Install Python 3.x: https://www.python.org/downloads/
2. Install the required libraries:
   ```
   pip install scapy ipwhois
   ```

## Usage

1. Save the provided code as a Python file (e.g., `main.py`).
2. Run the script:
   ```
   python main.py
   ```
3. The script will start capturing and displaying network packets.
4. Press `Ctrl+C` to stop the packet capture.

