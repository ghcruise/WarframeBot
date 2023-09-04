#旧API不使用
import requests
import os
import sys
from khl.card import CardMessage
sys.path.append(os.path.join(os.getcwd()))
from function.time2stamp import get_time_stamp

def nightwave():
    nora_raw = requests.get("https://api.warframestat.us/pc/zh/nightwave/")
    print("Status code:",nora_raw.status_code)
    nora_dict = nora_raw.json()

    totalChallenges = len(nora_dict['activeChallenges'])
    daliyChallenges = []
    weeklyChallenges = []
    i = 0


    while i < totalChallenges:
        if nora_dict['activeChallenges'][i]['isDaily']:
            daliyChallenges.append(nora_dict['activeChallenges'][i])
        else:
            weeklyChallenges.append(nora_dict['activeChallenges'][i])
        
        i += 1

    totalDaily = len(daliyChallenges)
    totalWeekly = len(weeklyChallenges)

    nightWaveCard = {
            "type": "card",
            "theme": "success",
            "size": "lg",
            "modules": [
            ]
        }

    daliy_i = 0
    weekly_i = 0

    while daliy_i < totalDaily:
        nightWaveContent = daliyChallenges[daliy_i]['title'] + " - " + str(daliyChallenges[daliy_i]['reputation']) +"声望\n" + daliyChallenges[daliy_i]['desc']
        nightwaveExpiry = get_time_stamp(daliyChallenges[daliy_i]['expiry']) * 1000
        nightWaveCard['modules'].append({
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": nightWaveContent
            }})
        nightWaveCard['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": nightwaveExpiry
            })
        daliy_i += 1

    while weekly_i < totalWeekly:
        nightWaveContent = weeklyChallenges[weekly_i]['title'] + " - " + str(weeklyChallenges[weekly_i]['reputation']) +"声望\n" + weeklyChallenges[weekly_i]['desc']
        nightwaveExpiry = get_time_stamp(weeklyChallenges[weekly_i]['expiry']) * 1000
        nightWaveCard['modules'].append({
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": nightWaveContent
            }})
        print(1)
        weekly_i += 1

    nightWaveCard['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": nightwaveExpiry
            })

    print(nightWaveCard)

    cm=CardMessage(nightWaveCard)
    return cm