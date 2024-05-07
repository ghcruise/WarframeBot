import os
import sys
import json
import datetime

def getArchimedea():
    with open("content/worldState.json",'r',encoding='utf-8') as f1:
        worldState_dict=json.load(f1)

    with open("translate/archimedea_tags.json",'r',encoding='utf-8') as f2:
        archimedea_tag=json.load(f2)

    now_time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    week5Time = 1714320000*1000
    timeDelta = int((now_time-week5Time)/604800000)
    print(timeDelta)
    weekNow = 5+timeDelta
    archimedea_string=worldState_dict['Tmp']
    tmp_dict=json.loads(archimedea_string)
    archimedea_dict=tmp_dict[f'lqo{weekNow}']


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

    archimedeaCard = [{
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

    num_dict = {0:"任务一:",1:"任务二:",2:"任务三:"}
    for i in range(3):
        archimedeaContent = f"{num_dict[i]} **{missionType[i]}**\n  - 任务偏差: {missionDeviation[i][0]}\n      - {missionDeviation[i][1]}\n  - 风险变量: {riskVariables[2*i][0]}\n      - {riskVariables[2*i][1]}\n  - 精英风险变量: {riskVariables[2*i+1][0]}\n      - {riskVariables[2*i+1][1]}"
        archimedeaCard[0]['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": archimedeaContent
            }
        })
    indvidualContent = f"**个人变量**:\n  {individualVariables[0][0]}\n      - {individualVariables[0][1]}\n  {individualVariables[1][0]}\n      - {individualVariables[1][1]}\n  {individualVariables[2][0]}\n      - {individualVariables[2][1]}\n  {individualVariables[3][0]}\n      - {individualVariables[3][1]}"
    archimedeaCard[0]['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": indvidualContent
            }
        })
    return archimedeaCard

print(getArchimedea())