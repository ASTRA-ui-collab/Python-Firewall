import json

RULES_FILE = "config/rules.json"

def load_rules():
    try:
        with open(RULES_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_rules(rules):
    with open(RULES_FILE, "w") as file:
        json.dump(rules, file, indent=4)

def add_rule(block_ip=None, block_port=None):
    rules = load_rules()
    rule = {}
    if block_ip:
        rule["block_ip"] = block_ip
    if block_port:
        rule["block_port"] = block_port
    rules.append(rule)
    save_rules(rules)

def list_rules():
    rules = load_rules()
    return rules

def remove_rule(index):
    rules = load_rules()
    if 0 <= index < len(rules):
        del rules[index]
        save_rules(rules)
