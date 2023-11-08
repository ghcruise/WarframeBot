import requests
import json
import sys
import os
from khl.card import CardMessage
sys.path.append(os.path.join(os.getcwd()))
from function.get_solnode_info import solNode
from function.translate_uni2zh import uni2zh

with open("content/extra/SolNode.json",'r',encoding='utf-8') as f:
    translateFaction = json.load(f)

def invasion():
    try:
        # worldState = requests.get("http://content.warframe.com/dynamic/worldState.php",timeout=(5,5))
        # worldState_dict = worldState.json()
        # print("[ init ] Invasions. Status Code:",worldState.status_code)
        with open("content/worldState.json",'r',encoding='utf-8') as f:
            worldState_dict=json.load(f)
        invasion_dict = worldState_dict['Invasions']

        nodeContent = []
        atkFaction = []
        atkProcess = []
        atkReward = []
        defFaction = []
        defProcess = []
        defReward = []
        i = 0
        while i<len(invasion_dict):
            defProcess_temp =int((invasion_dict[i]['Goal']-invasion_dict[i]['Count'])/(invasion_dict[i]['Goal'] * 2) * 100)
            if (defProcess_temp >= 100):
                i += 1
                continue
            else:
                defProcess.append(defProcess_temp)
                nodeInfo = solNode(invasion_dict[i]['Node'])
                nodeContent.append(nodeInfo['name']+" "+nodeInfo['systemName'])
                atkProcess.append(100 - defProcess_temp)
                atkFaction_temp =[obj for obj in translateFaction['missionFactions'] if obj['factionType']==invasion_dict[i]['Faction']]
                atkFaction.append(atkFaction_temp[0]['faction'])
                try:
                    atkReward_temp = f"{invasion_dict[i]['AttackerReward']['countedItems'][0]['ItemCount']}× {uni2zh(invasion_dict[i]['AttackerReward']['countedItems'][0]['ItemType'])}"
                except:
                    atkReward_temp = " "
                atkReward.append(atkReward_temp)
                
                defFaction_temp =[obj for obj in translateFaction['missionFactions'] if obj['factionType']==invasion_dict[i]['DefenderFaction']]
                defFaction.append(defFaction_temp[0]['faction'])
                try:
                    defReward_temp = f"{invasion_dict[i]['DefenderReward']['countedItems'][0]['ItemCount']}× {uni2zh(invasion_dict[i]['DefenderReward']['countedItems'][0]['ItemType'])}"
                except:
                    defReward_temp = " "
                defReward.append(defReward_temp)
                i += 1

        invasionCard = {
            "type": "card",
            "theme": "success",
            "size": "lg",
            "modules": [
            {
                "type": "section",
                "text": {
                "type": "paragraph",
                "cols": 3,
                "fields": [
                    {
                    "type": "kmarkdown",
                    "content": f"**进攻方**\n{atkFaction[0]}\n{atkProcess[0]} %\n{atkReward[0]}"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"\n**{nodeContent[0]}**\n**进度**\n**奖励**"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"**防守方**\n{defFaction[0]}\n{defProcess[0]} %\n{defReward[0]}"
                    }
                ]
                }
            }
            ]
        }

        i = 1
        while i<len(nodeContent):
            invasionCard['modules'].append({"type": "divider"})
            invasionCard["modules"].append({
                "type": "section",
                "text": {
                "type": "paragraph",
                "cols": 3,
                "fields": [
                    {
                    "type": "kmarkdown",
                    "content": f"{atkFaction[i]}\n{atkProcess[i]} %\n{atkReward[i]}"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"**{nodeContent[i]}**\n**进度**\n**奖励**"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"{defFaction[i]}\n{defProcess[i]} %\n{defReward[i]}"
                    }
                ]
                }
            }
            )
            i += 1
        
        invasionCard['modules'].append({"type": "divider"})
        invasionCard['modules'].append({
                "type": "section",
                "text": {
                "type": "paragraph",
                "cols": 2,
                "fields": [
                    {
                    "type": "kmarkdown",
                    "content": f"**巨人战舰**\n{round(worldState_dict['ProjectPct'][0],2)} %"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"**利刃豺狼**\n{round(worldState_dict['ProjectPct'][1],2)} %"
                    }]}})

        cm = CardMessage(invasionCard)
        invasionData = [nodeContent,atkFaction,atkProcess,atkReward,defFaction,defProcess,defReward]
        return cm,invasionData
    except:
        invasion()
# print(invasion()[0])