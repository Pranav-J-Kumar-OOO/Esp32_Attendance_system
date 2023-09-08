import urllib.request

def write(pin:int, data:int):
    with urllib.request.urlopen(f"https://blr1.blynk.cloud/external/api/update?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&v{pin}={data}") as response:
        pass