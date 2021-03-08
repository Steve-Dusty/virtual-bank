
import json as JSON

fp = open("file.json", mode="r")
jsonS = fp.read()
fp.close()
json = JSON.loads(jsonS)
json["steb"] = {"OMG": 1} # appends new element because bubby does not exist

fp = open("file.json", mode="w")
fp.write(JSON.dumps(json)) # new JSON object with an appended element
fp.close()