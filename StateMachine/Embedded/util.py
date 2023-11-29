import json
import requests

# SERVER = 'http://172.20.10.11:5000'
SERVER = 'http://172.20.10.3:5000'

def makeRequest(player: int, deltaPos: int, currPos: int):
    data = {
        "player": player,
        "deltaPos": deltaPos,
        "currPos": currPos
    }
    json_data = json.dumps(data)
    response = requests.post(f'{SERVER}/move', json=json_data)
    print(response)