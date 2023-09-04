#incomplete:古前中后排序、推送
#需要重构
import requests
import json
import os
import sys
from khl.card import CardMessage


sys.path.append(os.path.join(os.getcwd()))
from function.translateNode import translateNode
from function.time2stamp import get_time_stamp

with open('config/config.json', 'r', encoding='utf-8') as f1,\
    open('translate/translate_dict.json', 'r', encoding='utf-8') as f2:
    config = json.load(f1)
    translateDict = json.load(f2)

platform = config['platform']
def voidfissure(fissureType):
    voidfissure_raw = requests.get(f"https://api.warframestat.us/{platform}/en/fissures/")
    voidfissure_dict = voidfissure_raw.json()
    total_fissure = len(voidfissure_dict)

    print("[ init ] VoidFissures. Status code:",voidfissure_raw.status_code)

    i = 0
    hard_i = 0
    voidfissureHard_dict = {}
    storm_i = 0
    voidfissureStorm_dict = {}
    normal_i = 0
    voidfissureNormal_dict = {}

    while i < total_fissure:
        if voidfissure_dict[i]['isHard'] == True:
            voidfissureHard_dict[hard_i] = json.dumps(voidfissure_dict[i])
            hard_i += 1
            i += 1
        elif voidfissure_dict[i]['isStorm'] == True:
            voidfissureStorm_dict[storm_i] = json.dumps(voidfissure_dict[i])
            storm_i += 1
            i += 1
        else:
            voidfissureNormal_dict[normal_i] = json.dumps(voidfissure_dict [i])
            normal_i += 1
            i += 1

    normal_j = 0
    hard_j = 0
    storm_j = 0
    voidfissureNormal_content = []
    voidfissureNormal_expire = []
    voidfissureHard_content = []
    voidfissureHard_expire = []
    voidfissureStorm_content = []
    voidfissureStorm_expire = []

    while normal_j < normal_i:
        voidfissureNormal_content.append("\n"+translateDict[json.loads(voidfissureNormal_dict[normal_j])['tier']]+\
         " - "+translateDict[json.loads(voidfissureNormal_dict[normal_j])['missionKey']]+\
         " - "+translateNode(json.loads(voidfissureNormal_dict[normal_j])['nodeKey'])+\
         " - "+json.loads(voidfissureNormal_dict[normal_j])['enemyKey'])
        voidfissureNormal_expire.append(get_time_stamp(json.loads(voidfissureNormal_dict[normal_j])['expiry']) * 1000)
        normal_j += 1

    while hard_j < hard_i:
        voidfissureHard_content.append("\n"+translateDict[json.loads(voidfissureHard_dict[hard_j])['tier']]+\
         " - "+translateDict[json.loads(voidfissureHard_dict[hard_j])['missionKey']]+\
         " - "+translateNode(json.loads(voidfissureHard_dict[hard_j])['nodeKey'])+\
         "(钢铁之路) - "+json.loads(voidfissureHard_dict[hard_j])['enemyKey'])
        voidfissureHard_expire.append(get_time_stamp(json.loads(voidfissureHard_dict[hard_j])['expiry']) * 1000)
        hard_j += 1

    while storm_j < storm_i:
        voidfissureStorm_content.append("\n"+translateDict[json.loads(voidfissureStorm_dict[storm_j])['tier']]+\
         " - "+translateDict[json.loads(voidfissureStorm_dict[storm_j])['missionKey']]+\
         " - "+translateNode(json.loads(voidfissureStorm_dict[storm_j])['nodeKey'])+\
         "比邻星 - "+json.loads(voidfissureStorm_dict[storm_j])['enemyKey'])
        voidfissureStorm_expire.append(get_time_stamp(json.loads(voidfissureStorm_dict[storm_j])['expiry']) * 1000)
        storm_j += 1

    normal_j = 0
    voidfissureNormalCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        ]
    }
    while normal_j < normal_i:
        voidfissureNormalCard['modules'].append({
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": voidfissureNormal_content[normal_j]
            }
        })
        if (json.loads(voidfissureNormal_dict[normal_j])['expired'] == 1):
            voidfissureNormalCard['modules'].append({
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": " -已过期"
            }
        })
        else:
            voidfissureNormalCard['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": voidfissureNormal_expire[normal_j]
        })
        normal_j += 1
    cm_n = CardMessage(voidfissureNormalCard)

    #钢铁裂缝
    hard_j = 0
    voidfissureHardCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        ]
    }
    while hard_j < hard_i:
        voidfissureHardCard['modules'].append({
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": voidfissureHard_content[hard_j]
            }
        })
        if (json.loads(voidfissureHard_dict[hard_j])['expired'] == 1):
            voidfissureHardCard['modules'].append({
                "type": "section",
                "text": {
                "type": "plain-text",
                "content": " -已过期"
                }
        })
        else:
            voidfissureHardCard['modules'].append({
                "type": "countdown",
                "mode": "day",
                "endTime": voidfissureHard_expire[hard_j]
        })
        hard_j += 1
    cm_h = CardMessage(voidfissureHardCard)
    
    #虚空风暴
    storm_j = 0
    voidfissureStormCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        ]
    }
    while storm_j < storm_i:
        voidfissureStormCard['modules'].append({
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": voidfissureStorm_content[storm_j]
            }
        })
        if (json.loads(voidfissureStorm_dict[storm_j])['expired'] == 1):
            voidfissureStormCard['modules'].append({
                "type": "section",
                "text": {
                "type": "plain-text",
                "content": " -已过期"
                }
        })
        else:
            voidfissureStormCard['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": voidfissureStorm_expire[storm_j]
            })
        storm_j += 1
    cm_s = CardMessage(voidfissureStormCard)

    if fissureType == 0:
        return cm_n
    elif fissureType == 1:
        return cm_h
    elif fissureType == 2:
        return cm_s