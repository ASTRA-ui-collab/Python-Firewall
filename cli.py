import argparse
from rules import add_rule, list_rules, remove_rule

parser = argparse.ArgumentParser(description="Manage firewall rules")
parser.add_argument("--add-ip", help="Block an IP address")
parser.add_argument("--add-port", type=int, help="Block a specific port")
parser.add_argument("--list", action="store_true", help="List all rules")
parser.add_argument("--remove", type=int, help="Remove a rule by index")

args = parser.parse_args()

if args.add_ip:
    add_rule(block_ip=args.add_ip)
    print(f"Added rule: Block IP {args.add_ip}")

if args.add_port:
    add_rule(block_port=args.add_port)
    print(f"Added rule: Block Port {args.add_port}")

if args.list:
    rules = list_rules()
    for i, rule in enumerate(rules):
        print(f"[{i}] {rule}")

if args.remove is not None:
    remove_rule(args.remove)
    print(f"Removed rule at index {args.remove}")
