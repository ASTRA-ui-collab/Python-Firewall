# Python Firewall  

A lightweight, rule-based firewall built with Python to block specific IP addresses, ports, and protocols. This firewall uses **Scapy** and **NetfilterQueue** to filter network traffic dynamically.  

## **Features**  
✅ Block traffic based on IP address and ports  
✅ Manage rules dynamically using a command-line interface (CLI)  
✅ Log blocked packets in **plain text** and **JSON format**  
✅ Lightweight and easy to set up  

---

## **Installation**  

### **Prerequisites**  
- Python 3.8+  
- `iptables` (Linux) or `netsh` (Windows)  
- `pip` for installing dependencies  

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/python-firewall.git
cd python-firewall

dependencies
pip install -r requirements.txt
