import os
import sys
import json
import requests

sys.path.append(os.path.join(os.getcwd()))
from function.translate_uni2zh import uni2zh
from function.get_solnode_info import solNode
with open("translate/translate_event.json",'r',encoding="utf-8") as f:
    eventDict = json.load(f)
def event():
    # worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    # worldState_dict = worldState.json()
    # print("[ init ] Events. Status Code:",worldState.status_code)
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)

    event_dict = worldState_dict['Goals']

    eventID = []
    eventNodes= []
    eventExpiry = []
    eventTag = []
    eventRewards = []
    for i in range(len(event_dict)):
        eventID.append(event_dict[i]['_id']['$oid'])
        try:
            #eventNodes.append(f"{solNode(event_dict[i]['Node'])['name']} {solNode(event_dict[i]['Node'])['systemName']}")
            None
        except:
            #eventNodes.append(f"{solNode(event_dict[i]['VictimNode'])['name']} {solNode(event_dict[i]['VictimNode'])['systemName']}")
            None
        eventExpiry.append(event_dict[i]['Expiry']['$date']['$numberLong'])
        eventTag.append(event_dict[i]['Tag'])
        try:
            eventRewards.append(uni2zh(event_dict[i]['Reward']['items'][0].replace('/Lotus/StoreItems','/Lotus')))
        except:
            eventRewards.append("null")

    eventData = [eventID,eventNodes,eventTag,eventExpiry,eventRewards]
    eventCard = [{
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": []
    }]
    for i in range(len(event_dict)):
        eventContent = f"[{eventDict.get(eventTag[i],eventTag[i])}]\n - 奖励: {eventRewards[i]}\n"
        eventCard[0]['modules'].append(
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": eventContent
            }})
    return eventCard,eventData   
# print(event()[0])