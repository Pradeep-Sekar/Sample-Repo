# #! python3


import requests

# print("Hello World!")
r = requests.get("https://docs.anaconda.com/anaconda/install/windows/")
print(r.status_code)
print(r.ok)
