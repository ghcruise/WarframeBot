import json
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from api_module.voidFissures import getFissures
from function.get_solnode_info import solNode

print("[ init ] Push Fissures.")
voidDict = {"VoidT1":"古纪","VoidT2":"前纪","VoidT3":"中纪","VoidT4":"后纪","VoidT5":"安魂"}

def findNode(i,list:list):
    try:
        _ = list.index(i)
        return True
    except:
        return False

def fissurePush():
    with open("config/config.json",'r',encoding='utf-8') as f:
        config = json.load(f)

    pushFissures = config['fissures']
    pushFissuresN = pushFissures['voidfissures_normal']
    pushFissuresH = pushFissures['voidfissures_hard']

    fissuresN = getFissures()[3]
    fissuresH = getFissures()[4]

    pushListN = [obj for obj in fissuresN if (findNode(obj['Node'],pushFissuresN) is True)]
    pushListH = [obj for obj in fissuresH if (findNode(obj['Node'],pushFissuresH) is True)]
    pushList = pushListN+pushListH

    id = []
    content = []
    expiry = []
    sortedFissures = []
    for i in range(len(pushList)):
        id.append(pushList[i]['_id']['$oid'])
        nodeContent = solNode(pushList[i]['Node'])
        expiry.append(int(pushList[i]['Expiry']['$date']['$numberLong']))
        try:
            _ = pushList[i]['Hard']
            content.append(f"{voidDict[pushList[i]['Modifier']]} - {nodeContent['type']} - {nodeContent['faction']}\n {nodeContent['name']} - {nodeContent['systemName']}(钢铁之路)")
        except:
            content.append(f"{voidDict[pushList[i]['Modifier']]} - {nodeContent['type']} - {nodeContent['faction']}\n {nodeContent['name']} - {nodeContent['systemName']}")
        sortedFissures.append([{
                    "type": "card",
                    "theme": "warning",
                    "size": "lg",
                    "modules": [{
                    "type": "section",
                    "text": {
                        "type": "kmarkdown",
                        "content": content[i]
                    }},
                    {
                    "type": "countdown",
                    "mode": "day",
                    "endTime": expiry[i]
                    }]}])
    # print(sortedFissures)
    # print(id)
    return sortedFissures,id

