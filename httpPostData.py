import urllib.request
import json

body = {'key': 'T7H40F0X82VGW7L5', 'field1': 20, "field2": 35}
myurl = "https://api.thingspeak.com/update"

req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8') 
jsonDataAsBytes = json.dumps(body).encode('utf-8') 
req.add_header('Content-Length', len(jsonDataAsBytes))
response = urllib.request.urlopen(req, jsonDataAsBytes)