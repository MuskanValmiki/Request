import requests
import json
url = requests.get("http://join.navgurukul.org/api/partners")
data = url.json()
dict = {}
list = []
for key in data:
    index = 0
    while index < len(data[key]):
        for key1 in data[key][index]:
            if key1 == "name":
                list.append(index + 1)
                list.append(data[key][index][key1])
        dict["Partner"] = list
        index += 1
with open("request_test.json","w") as file:
    json.dump(dict,file,indent = 4)



