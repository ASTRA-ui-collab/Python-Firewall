import scapy.all as scapy
import netfilterqueue
import json
from logger import log_event
from rules import load_rules

def process_packet(packet):
    pkt = scapy.IP(packet.get_payload())  # Convert raw packet
    rules = load_rules()

    for rule in rules:
        if (pkt.src == rule.get("block_ip") or pkt.dst == rule.get("block_ip")) or \
           (pkt.haslayer(scapy.TCP) and pkt.dport == rule.get("block_port", -1)) or \
           (pkt.haslayer(scapy.UDP) and pkt.dport == rule.get("block_port", -1)):
            log_event(f"Blocked {pkt.src} -> {pkt.dst} | Port: {pkt.dport}")
            packet.drop()  # Drop packet
            return
    
    packet.accept()  # Allow packet

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)

try:
    print("[*] Firewall Running...")
    queue.run()
except KeyboardInterrupt:
    print("\n[*] Stopping Firewall")
