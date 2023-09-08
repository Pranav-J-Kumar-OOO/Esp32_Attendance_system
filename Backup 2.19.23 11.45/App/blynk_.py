import urllib.request
import requests
import json

def writeInt(pin:int, data:int):
    with urllib.request.urlopen(f"https://blr1.blynk.cloud/external/api/update?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&v{pin}={data}") as response:
        pass
def writeStr(pin:int, data:str):
    with urllib.request.urlopen(f"https://blr1.blynk.cloud/external/api/update?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&v{pin}={data}") as response:
        pass
def retriveStr(pin:int, auth:str):
    i = requests.get(f"https://blr1.blynk.cloud/external/api/get?token={auth}&v{pin}")
    return i.text