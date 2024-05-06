import os
import sys
import json
import datetime

def getArchimedea():
    with open("content/worldState.json",'r',encoding='utf-8') as f1:
        worldState_dict=json.load(f1)
        archimedea_string=worldState_dict['Tmp']
        tmp_dict=json.loads(archimedea_string)
        archimedea_dict=tmp_dict['lqo6']

    with open("translate/archimedea_tags.json",'r',encoding='utf-8') as f2:
        archimedea_tag=json.load(f2)

    missionType = []
    missionDeviation=[]
    riskVariables=[]
    individualVariables=[]
    for i in range(len(archimedea_dict['mt'])):
        missionType.append(archimedea_tag['missionType'].get(archimedea_dict['mt'][i],archimedea_dict['mt'][i]))
        missionDeviation.append(archimedea_tag['missionDeviation'].get(archimedea_dict['mv'][i],[archimedea_dict['mv'][i],archimedea_tag['missionDeviation']['Tag'][1]]))
        for j in range(2):
            riskVariables.append(archimedea_tag['riskVariables'].get(archimedea_dict['c'][i][j],[archimedea_dict['c'][i][j],archimedea_tag['riskVariables']['Tag'][1]]))
    for i in range(4):
        individualVariables.append(archimedea_tag['individualVariables'].get(archimedea_dict['fv'][i],[archimedea_dict['fv'][i],archimedea_tag['individualVariables']['Tag'][1]]))

    archonCard = [{
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"**精英科研**"
            }
        }]
        }]

    num_dict = {"0":"任务一:","1":"任务二:","2":"任务三:"}
    for i in range(3):
        archonContent = f"{num_dict[f'{i}']} {missionType[i]}"
        archonCard[0]['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": archonContent
            }
        })
    archonCard[0]['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": archonExpiry
        })
    return archonCard

getArchimedea()