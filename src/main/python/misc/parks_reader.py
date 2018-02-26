import json

with open('parks.json') as parks_f:
    parks_json = json.load(parks_f)

# print all parks that do not have lat and long data
for p in parks_json['data']:
    if not p['latLong'].strip():
        print p['fullName']
