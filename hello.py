# #! python3
import math
import os
import sys

import requests

print("Hello World!")
r = requests.get("https://docs.anaconda.com/anaconda/install/windows/")
print(r.status_code)
