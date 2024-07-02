from scapy.all import sniff, IP, TCP, UDP, ICMP
from ipwhois import IPWhois

def get_geolocation(ip_addr):
    try:
        obj = IPWhois(ip_addr)
        result = obj.lookup_whois()
        return f"{result['nets'][0]['country']}, {result['nets'][0]['city']}"
    except:
        return "Unknown"

def packet_callback(packet):
    if IP in packet:
        print(f"Protocol: {packet[IP].proto}")
        print(f"Source IP : {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Source Location: {get_geolocation(packet[IP].src)}")
        print(f"Destination Location: {get_geolocation(packet[IP].dst)}")

        if TCP in packet:
                print(f"Source Port: {packet[TCP].sport}")
                print(f"Destination Port: {packet[TCP].dport}")
                print(f"TCP Flags: {packet[TCP].flags}")
                print(f"Payload: {packet[TCP].payload}")

        elif UDP in packet:
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print(f"ICMP type:{packet[ICMP].type}")
            print(f"ICMP code:{packet[ICMP].code}")

        print('-'*50)

sniff(filter="ip",prn=packet_callback, count=0)