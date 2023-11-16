# 需要重构
# To be rebuild
# 1700020800 anger ends, envy start
#  Joy -> Anger -> Envy -> Sorrow ->Fear
import re
import json
import sys
import os
import requests
import datetime
from khl.card import CardMessage
sys.path.append(os.path.join(os.getcwd()))
from function.time2stamp import get_time_stamp

with open('config/config.json', 'r', encoding='utf-8') as f1,\
    open('translate/translate_dict.json', 'r', encoding='utf-8') as f2,\
    open('translate/translate_catagory.json', 'r', encoding='utf-8') as f3:

    config = json.load(f1)
    translateDict = json.load(f2)
    translateCatagory = json.load(f3)

platform = config['platform']

def plain():
    now_time = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
    cetusCycle = requests.get(f"https://api.warframestat.us/{platform}/cetusCycle")
    solarisCycle = requests.get(f"https://api.warframestat.us/{platform}/vallisCycle")
    zarimanCycle = requests.get(f"https://api.warframestat.us/{platform}/zarimanCycle")
    duviriCycle = requests.get(f"https://api.warframestat.us/{platform}/duviriCycle")
    cetusCycle_dict = cetusCycle.json()
    solarisCycle_dict = solarisCycle.json()
    zarimanCycle_dict = zarimanCycle.json()
    duviriCycle_dict = duviriCycle.json()
    print("[ init ] Plains. Status code:",cetusCycle.status_code)
    
    #地球、火卫2
    if cetusCycle_dict['state']== "day":
        cetusState = "**白天**"
        deimosState = "**FASS**"
    else:
        cetusState = "**夜晚**"
        deimosState = "**VOME**"
    cetusCycle_process = re.findall(r'\d+', cetusCycle_dict['id'])
    cetusCycleCD = int(cetusCycle_process[0])

    #金星
    if solarisCycle_dict['state']=="cold":
        solarisState = "**寒冷**"
    else:
        solarisState = "**温暖**"
    solarisCycleCD = int(get_time_stamp(solarisCycle_dict['expiry'])*1000)

    #扎里曼
    if zarimanCycle_dict['state']=="corpus":
        zarimanState = "**Corpus**"
    else:
        zarimanState = "**Grineer**"
    zarimanCycleCD = int(get_time_stamp(zarimanCycle_dict['expiry'])*1000)

    #双衍王境
    if duviriCycle_dict['state']=="fear":
        duviriState = "**恐惧**"
    elif duviriCycle_dict['state']=="sorrow":
        duviriState = "**悲伤**"
    elif duviriCycle_dict['state']=="joy":
        duviriState = "**喜悦**"
    elif duviriCycle_dict['state']=="anger":
        duviriState = "**愤怒**"
    elif duviriCycle_dict['state']=="envy":
        duviriState = "**嫉妒**"
    duviriCycleCD = int(get_time_stamp(duviriCycle_dict['expiry'])*1000)


    #处理卡片消息
    cetusCycleContent=f"希图斯/夜灵平野时间为:\n - {cetusState}"
    deimosStateContent = f"殁世幽都/魔胎之境循环为:\n - {deimosState}"
    solarisStateContent = f"福尔图纳/奥布山谷环境为:\n - {solarisState}"
    zarimanStateContent = f"扎里曼号入侵状态为:\n - {zarimanState}"
    duviriStateContent = f"双衍王境复眠螺旋为:\n - {duviriState}"
    #print(cetusCycleContent)
    cetusCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": cetusCycleContent
            }
        },
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": deimosStateContent
            }
        }]}
    
    if now_time<cetusCycleCD:
        cetusCard['modules'].append({
        "type": "countdown",
        "mode": "day",
        "endTime": cetusCycleCD
        })
    else:
        cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": " - 已过期"
            }})
        
    cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": solarisStateContent
            }})
    if now_time<solarisCycleCD:
        cetusCard['modules'].append({
        "type": "countdown",
        "mode": "day",
        "endTime": solarisCycleCD
        })
    else:
        cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": " - 已过期"
            }})
        
    cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": zarimanStateContent
            }})
    if now_time<zarimanCycleCD:
        cetusCard['modules'].append({
        "type": "countdown",
        "mode": "day",
        "endTime": zarimanCycleCD
        })
    else:
        cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": " - 已过期"
            }})
        
    cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": duviriStateContent
            }})
    if now_time<duviriCycleCD:
        cetusCard['modules'].append({
        "type": "countdown",
        "mode": "day",
        "endTime": duviriCycleCD
        })
    else:
        cetusCard['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": " - 已过期"
            }})

    cm = CardMessage(cetusCard)
    return cm

# print(plain())