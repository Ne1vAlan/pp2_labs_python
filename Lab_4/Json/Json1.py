import json

with open(r"D:\gitHub\pp2_labs_python\Lab_4\Json\sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 85)
print(f"{'DN':<55} {'Description':<20} {'Speed':<8} {'MTU'}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else "inherit"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<55} {description:<20} {speed:<8} {mtu}")