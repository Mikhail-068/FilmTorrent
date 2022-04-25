import time
import json
TIME = time.strftime('%H.%M_%d.%b')
dic = {
    'one': 1
}

with open(f"Data/Page{time.strftime('%H.%M_%d.%b')}.json", 'w') as file:
    json.dump(dic, file, indent=2, ensure_ascii=False)