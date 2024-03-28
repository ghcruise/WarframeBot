#官方API
# import requests
import os
import sys
import json
import datetime

sys.path.append(os.path.join(os.getcwd()))
from function.get_solnode_info import solNode

voidDict = {"VoidT1":"古纪","VoidT2":"前纪","VoidT3":"中纪","VoidT4":"后纪","VoidT5":"安魂","VoidT6":"全能"}
print("[ init ] Voidfissures.")

def getFissures():
    # worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    # worldState_dict = worldState.json()
    # print("[ VoidFissures ] Status Code:",worldState.status_code)
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)
    with open("content/extra/SolNode.json",'r',encoding='utf-8') as f0:
        sol_info = json.load(f0)

    fissures_dict = worldState_dict['ActiveMissions']
    fissures_dict = sorted(fissures_dict, key=lambda x : x['Region'], reverse=False)
    storms_dict = worldState_dict['VoidStorms']
    timeNow = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    print(f"{datetime.datetime.now()} [Voidfissures] Now time:{timeNow}")
    for i in range(len(storms_dict)):
        storms_dict[i]['Region'] = solNode(storms_dict[i]['Node'])['Region']
    storms_dict = sorted(storms_dict, key=lambda x : x['Region'], reverse=False)

    voidT1 = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT1" and obj.get('Hard') is None)]
    voidT2 = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT2" and obj.get('Hard') is None)]
    voidT3 = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT3" and obj.get('Hard') is None)]
    voidT4 = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT4" and obj.get('Hard') is None)]
    voidT5 = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT5" and obj.get('Hard') is None)]
    voidT6 = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT6" and obj.get('Hard') is None)]
    voidT1h = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT1" and obj.get('Hard') is True)]
    voidT2h = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT2" and obj.get('Hard') is True)]
    voidT3h = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT3" and obj.get('Hard') is True)]
    voidT4h = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT4" and obj.get('Hard') is True)]
    voidT5h = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT5" and obj.get('Hard') is True)]
    voidT6h = [obj for obj in fissures_dict if (obj['Modifier']=="VoidT6" and obj.get('Hard') is True)]
    voidT1s = [obj for obj in storms_dict if obj['ActiveMissionTier']=="VoidT1"]
    voidT2s = [obj for obj in storms_dict if obj['ActiveMissionTier']=="VoidT2"]
    voidT3s = [obj for obj in storms_dict if obj['ActiveMissionTier']=="VoidT3"]
    voidT4s = [obj for obj in storms_dict if obj['ActiveMissionTier']=="VoidT4"]

    voidFissureN = voidT1+voidT2+voidT3+voidT4+voidT5+voidT6
    voidFissureH = voidT1h+voidT2h+voidT3h+voidT4h+voidT5h+voidT6h
    voidFissureS = voidT1s+voidT2s+voidT3s+voidT4s

    NCard = [{
                "type": "card",
                "theme": "success",
                "size": "lg",
                "modules": [
                ]
            }]
    for i in range(len(voidFissureN)):
        if timeNow >= int(voidFissureN[i]['Expiry']['$date']['$numberLong']):
            continue
        else:
            nodeContent = solNode(voidFissureN[i]['Node'])
            nodeType = voidFissureN[i]['MissionType']
            MT =[obj for obj in sol_info['missionTypes'] if obj['missionType']==nodeType]
            cardContent = f"{voidDict[voidFissureN[i]['Modifier']]} - {MT[0]['type']} - {nodeContent['faction']}\n {nodeContent['name']} - {nodeContent['systemName']}"
            NCard[0]['modules'].append({
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": cardContent
                }})
            NCard[0]['modules'].append({
                "type": "countdown",
                "mode": "day",
                "endTime": int(voidFissureN[i]['Expiry']['$date']['$numberLong'])
            })
            NCard[0]['modules'].append({"type": "divider"})
    NCard[0]['modules'].append(
    {
        "type": "action-group",
        "elements": [
        {
            "type": "button",
            "theme": "secondary",
            "value": "0",
            "text": {
            "type": "plain-text",
            "content": "虚空裂缝(当前)"
            }
        },
        {
            "type": "button",
            "theme": "warning",
            "value": "1",
            "click": "return-val",
            "text": {
            "type": "plain-text",
            "content": "钢铁裂缝"
            }
        },
        {
            "type": "button",
            "theme": "info",
            "value": "2",
            "click": "return-val",
            "text": {
            "type": "plain-text",
            "content": "虚空风暴"
            }
        }
        ]
    })

    HCard = [{
                "type": "card",
                "theme": "success",
                "size": "lg",
                "modules": [
                ]
            }]
    for i in range(len(voidFissureH)):
        if timeNow >= int(voidFissureH[i]['Expiry']['$date']['$numberLong']):
            continue
        else:
            nodeContent = solNode(voidFissureH[i]['Node'])
            nodeType = voidFissureH[i]['MissionType']
            MT =[obj for obj in sol_info['missionTypes'] if obj['missionType']==nodeType]
            cardContent = f"{voidDict[voidFissureH[i]['Modifier']]} - {nodeContent['type']} - {nodeContent['faction']}\n {nodeContent['name']} - {nodeContent['systemName']}(钢铁之路)"
            HCard[0]['modules'].append({
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": cardContent
                }})
            HCard[0]['modules'].append({
                "type": "countdown",
                "mode": "day",
                "endTime": int(voidFissureH[i]['Expiry']['$date']['$numberLong'])
            })
            HCard[0]['modules'].append({"type": "divider"})
    HCard[0]['modules'].append(
    {
        "type": "action-group",
        "elements": [
        {
            "type": "button",
            "theme": "primary",
            "value": "0",
            "click": "return-val",
            "text": {
            "type": "plain-text",
            "content": "虚空裂缝"
            }
        },
        {
            "type": "button",
            "theme": "secondary",
            "value": "1",
            "text": {
            "type": "plain-text",
            "content": "钢铁裂缝(当前)"
            }
        },
        {
            "type": "button",
            "theme": "info",
            "value": "2",
            "click": "return-val",
            "text": {
            "type": "plain-text",
            "content": "虚空风暴"
            }
        }
        ]
    })

    SCard = [{
                "type": "card",
                "theme": "success",
                "size": "lg",
                "modules": [
                ]
            }]
    for i in range(len(voidFissureS)):
        if timeNow >= int(voidFissureS[i]['Expiry']['$date']['$numberLong']):
            continue
        else:
            nodeContent = solNode(voidFissureS[i]['Node'])
            cardContent = f"{voidDict[voidFissureS[i]['ActiveMissionTier']]} - {nodeContent['type']} - {nodeContent['faction']}\n {nodeContent['name']}"
            SCard[0]['modules'].append({
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": cardContent
                }})
            SCard[0]['modules'].append({
                "type": "countdown",
                "mode": "day",
                "endTime": int(voidFissureS[i]['Expiry']['$date']['$numberLong'])
            })
            SCard[0]['modules'].append({"type": "divider"})
    SCard[0]['modules'].append(
    {
        "type": "action-group",
        "elements": [
        {
            "type": "button",
            "theme": "primary",
            "value": "0",
            "click": "return-val",
            "text": {
            "type": "plain-text",
            "content": "虚空裂缝"
            }
        },
        {
            "type": "button",
            "theme": "warning",
            "value": "1",
            "click": "return-val",
            "text": {
            "type": "plain-text",
            "content": "钢铁裂缝"
            }
        },
        {
            "type": "button",
            "theme": "secondary",
            "value": "2",          
            "text": {
            "type": "plain-text",
            "content": "虚空风暴(当前)"
            }
        }
        ]
    })
    # print(NCard)
    return NCard,HCard,SCard,voidFissureN,voidFissureH
    
#print(getFissures()[1])