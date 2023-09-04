#午夜电波官方API
import requests
import os
import sys
import json
import re
#查询电波奖励TODO
sys.path.append(os.path.join(os.getcwd()))
from function.time2stamp import get_time_stamp

with open("content/ExportSortieRewards_zh.json",'r',encoding='utf-8') as f:
    translateChallenge = json.load(f)

def nightWave():
    worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    worldState_dict = worldState.json()
    print("[ init ] NightWave. Status Code:",worldState.status_code)
    nightWave_dict = worldState_dict['SeasonInfo']['ActiveChallenges']
    # print(len(nightWave_dict))

    challengeName = []
    challengeContent = []
    standing = []
    expiry = []
    for i in range(len(nightWave_dict)):
        result = [obj for obj in translateChallenge['ExportNightwave']['challenges'] if obj['uniqueName']==nightWave_dict[i]['Challenge']]
        expiry.append(nightWave_dict[i]['Expiry']['$date']['$numberLong'])
        challengeName.append(result[0]['name'])
        challengeContent.append(re.sub(r'\<[\w]+\>',"",str(re.sub(r'\|[^|]+\|',str(result[0]['required']),result[0]['description']))))
        standing.append(result[0]['standing'])

    noraCard = {
                "type": "card",
                "theme": "success",
                "size": "lg",
                "modules": [
            ]}

    for i in range(len(nightWave_dict)):
        noraContent = f"{challengeName[i]} - {standing[i]} 声望\n - {challengeContent[i]}"
        noraExpiry = expiry[i]
        noraCard['modules'].append({
                "type": "section",
                "text": {
                "type": "kmarkdown",
                "content": noraContent
                }})
        try:
            nightWave_dict[i]['Daily']
            noraCard['modules'].append({
                "type": "countdown",
                "mode": "day",
                "endTime": noraExpiry
                })
        except:
            pass
        if i != len(nightWave_dict)-1:
            noraCard['modules'].append({"type": "divider"})
        else:
            noraCard['modules'].append({
                "type": "countdown",
                "mode": "day",
                "endTime": noraExpiry
                })          
    return [noraCard]
# print(nightWave())