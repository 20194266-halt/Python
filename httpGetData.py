import urllib.request
import json
import time

while True:
    TS = urllib.request.urlopen("https://api.thingspeak.com/channels/1529099/feeds.json?results=2")
    response = TS.read()
    data=json.loads(response)
    print("Created at: " + data["feeds"][0]["created_at"]+ "\n" +"Data:"
          " {field1: "+ data["feeds"][0]["field1"]+ 
          " field2: " + data["feeds"][0]["field2"] +"}")
   
    TS.close()
    break