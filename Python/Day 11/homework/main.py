import tracker
import json
from datetime import datetime

records=[
    tracker.record("Trivandrum", "Beaches and rich cultural heritage", "12-03-2024"),
    tracker.record("Kochi", "Backwaters and historic Fort Kochi", "05-06-2024"),
    tracker.record("Munnar", "Hill station with tea gardens", "18-08-2024")
    ]
for i in records:
    dt_obj = datetime.strptime(i["date"], "%d-%m-%Y")
    i["date"]= dt_obj.strftime("%B %d, %Y")


json_data = json.dumps(records)
print("JSON Output:",json_data)

parsed = json.loads(json_data)
print("\nParsed Records:")
for k in parsed:
    print(k)

