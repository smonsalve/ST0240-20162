import json

archivo = open("stations.json",'r')

lineas = " "

for line in archivo:
    lineas +=  line

a = json.loads(lineas)

#print a["features"][0]

totalDocks = 0

for item in a["features"]:
    b =  item["properties"]["totalDocks"]
    totalDocks += b

print totalDocks
