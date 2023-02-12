# Monday 30/01/2923 - Afternoon Exercises
import requests
import json  # json data types: number, string, boolean, array, object, null

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

post_codes_dict = post_codes_req.json()
# print(post_codes_dict["result"])

data = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
print(data)
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=data)

print(post_multi_req.json()["result"][0]["query"])
