import datetime
import json
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from function.get_solnode_info import solNode
from function.translate_uni2zh import uni2zh
with open("content/extra/SolNode.json",'r',encoding='utf-8') as f:
    nodeInfo_dict = json.load(f)
alert_translate = {"LotusGift":"Lotus的赏赐"}
print("[ init ] Alerts.")

def alert():
    # worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    # worldState_dict = worldState.json()
    # print("[ init ] Alerts. Status Code:",worldState.status_code)
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)
    alert_dict = worldState_dict['Alerts']

    alertID = []
    alertNodes= []
    alertertExpiry = []
    alertTag = []
    alertRewards = []
    for i in range(len(alert_dict)):
        alertID.append(alert_dict[i]['_id']['$oid'])
        nodeFactorInfo = [obj for obj in nodeInfo_dict['missionFactions'] if obj['factionType']==alert_dict[i]['MissionInfo']['faction']]
        nodeMissionInfo = [obj for obj in nodeInfo_dict['missionTypes'] if obj['missionType']==alert_dict[i]['MissionInfo']['missionType']]
        alertNodes.append(f"{solNode(alert_dict[i]['MissionInfo']['location'])['name']} {solNode(alert_dict[i]['MissionInfo']['location'])['systemName']} - {nodeFactorInfo[0]['faction']}\n - {nodeMissionInfo[0]['type']}")
        alertertExpiry.append(alert_dict[i]['Expiry']['$date']['$numberLong'])
        alertTag.append(alert_translate.get(alert_dict[i]['Tag'],alert_dict[i]['Tag']))
        try:
            reward = alert_dict[i]['MissionInfo']['missionReward']['items'][0]
            alertRewards.append(uni2zh(reward.replace("/Lotus/StoreItems",'/Lotus')))
        except:
            reward = alert_dict[i]['MissionInfo']['missionReward']['countedItems'][0]
            alertRewards.append(f"{reward['ItemCount']}× {uni2zh(reward['ItemType'].replace('/Lotus/StoreItems','/Lotus'))}")
    
    alertCard = [{
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": []
    }]
    for i in range(len(alert_dict)):
        alertContent = f"[{alertTag[i]}]\n{alertNodes[i]}\n - 奖励：{alertRewards[i]}"
        alertCard[0]['modules'].append(
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": alertContent
            }})
        alertCard[0]['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": int(alertertExpiry[i])
        })
        print(f"{datetime.datetime.now()} [Alerts] Done")
    return alertCard

# print(alert())