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

Here’s the **USAGE.md** in one copy-paste block:  

```md
# Python Firewall - Usage Guide  

This document explains how to use and configure the Python Firewall.  

---

## **1. Running the Firewall**  
To start monitoring traffic, run:  
```bash
sudo python3 src/firewall.py
```
The script will continuously check packets and apply rules.

---

## **2. Managing Firewall Rules**  
You can add, remove, and list rules using `cli.py`.  

### **Adding Rules**  
#### **Block an IP**  
```bash
python3 src/cli.py --add-ip 192.168.1.100
```
#### **Block a Port**  
```bash
python3 src/cli.py --add-port 80
```

---

### **Listing Current Rules**  
```bash
python3 src/cli.py --list
```
Example output:
```
[0] {'block_ip': '192.168.1.100'}
[1] {'block_port': 80}
```

---

### **Removing a Rule**  
To remove rule **[0]**, run:  
```bash
python3 src/cli.py --remove 0
```

---

## **3. Logs & Debugging**  
All blocked traffic is logged in `logs/`.  

To view logs in real-time:  
```bash
tail -f logs/firewall.log
```

For JSON logs:  
```bash
cat logs/firewall.json | jq
```

---

## **4. Troubleshooting**  
#### **Permission Denied Error**  
Make sure you are running the firewall with **sudo**:  
```bash
sudo python3 src/firewall.py
```

#### **Firewall Not Blocking Traffic?**  
1. Check `iptables` rules:  
   ```bash
   sudo iptables -L
   ```
2. Verify the rule exists in `rules.json`.  

---

