import csv
import random

data = [
    ["Ahmedabad", "Baroda", "Avadhoot Agro Sales", "10006413", 1],
    ["Akola", "Amravati", "Bajaj Seeds  & Pesticides", "10005955", 5],
    ["Bathinda", "Abohar", "Garg Agro Chemicals", "10001552", 2]
]

regions = ["Ahmedabad", "Akola", "Bathinda", "Pune", "Delhi", "Chennai"]
territories = ["Baroda", "Amravati", "Abohar", "West", "North", "South"]
names = ["Agro Sales", "Seeds & Pesticides", "Agro Chemicals", "Farmers Hub", "Kisan Store", "Green World"]

for i in range(100):
    data.append([
        random.choice(regions),
        random.choice(territories),
        f"{random.choice(names)} {i}",
        f"2000{i:04d}",
        random.randint(1, 10)
    ])

with open('/Users/ankush/Desktop/Sumil Lucky Draw/master_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Region", "Territory", "CUSTOMER NAME", "CUSTOMER CODE", "Sum of Max Coupons"])
    for row in data:
        writer.writerow(row)

print("Created master_data.csv")
