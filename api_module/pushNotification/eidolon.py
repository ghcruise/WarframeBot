import json
import datetime
from khl.card import CardMessage

def eidolonHunter():
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)
    cetus_raw = [obj for obj in worldState_dict['SyndicateMissions'] if obj['Tag']=="CetusSyndicate"]
    cetus_time_up = int(cetus_raw[0]['Expiry']['$date']['$numberLong'])
    #print(cetus_time_up)
    now_time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    #print(cetus_time_up)
    #print(now_time)
    time2tomrrow = cetus_time_up - now_time
    #print(time2tomrrow)
    night_time = cetus_time_up - 3000000
    if ((time2tomrrow>=3000000) and (time2tomrrow<=4200000)):
        readyHunting = 1
    else:
        readyHunting = 0
    # print("readyhunting:",readyHunting)
    eidolonCard = {
        "type": "card",
        "theme": "info",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": "**夜灵平原即将入夜**"
            }
        },
        {
            "type": "countdown",
            "mode": "day",
            "endTime": night_time
        },
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": "距离下一天:"
            }
        },
        {
            "type": "countdown",
            "mode": "day",
            "endTime": cetus_time_up
        }
        ]
    }
    cm = CardMessage(eidolonCard)
    return cm,readyHunting

#print(f"result: {eidolonHunter()}")