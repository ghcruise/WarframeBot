import json
import sys
import os
import datetime
sys.path.append(os.path.join(os.getcwd()))

timeNow = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
print(timeNow)

#func
def get_cycle():
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)

    state_info = [obj for obj in worldState_dict['SyndicateMissions'] if obj['Tag']=="CetusSyndicate"]
    dayStart = int(state_info[0]['Activation']['$date']['$numberLong'])
    dayEnd = int(state_info[0]['Expiry']['$date']['$numberLong'])
    # print([dayStart,dayEnd])
    cycleCard = [{
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": []}]

    # Cytus & Entrati : No paradox. Done. 
    dayDuration = dayEnd - dayStart
    cytusTimeDelta = timeNow - dayStart
    cytusDaytime = 100 * 60 * 1000
    if cytusTimeDelta < 6000000:
        cytusTime = "白天"
        entratiTime = "Fass"
        cytusExpiry = dayEnd - 3000000
    else:
        cytusTime = "夜晚"
        entratiTime = "Vome"
        cytusExpiry = dayEnd
    # print([cytusTime,cytusExpiry])
    cytusCard = [{
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"希图斯/夜灵平野时间为:\n - **{cytusTime}**"
            }
        },
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"殁世幽都/魔胎之境循环为:\n - **{entratiTime}**"
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": cytusExpiry
        },
        {"type": "divider"}
        ]

    # Solaris: Need calculate.
    # A cycle: 26m 40s
    # Warm 6m 40s
    # Cold 20m
    # 1700050400000
    # 2023-11-15 20:13:20 -> warm start
    # 1700050800000 -> cold start
    solarisStatus = {0:"寒冷",1:"温暖"}
    solarisTimeDelta = timeNow - 1700050800000
    solarisStatusType = int(solarisTimeDelta/1600000)%2
    solarisTime = solarisStatus[solarisStatusType]
    if solarisStatusType == 0:
        solarisExpiry = timeNow - solarisTimeDelta%1600000 +1200000
    else:
        solarisExpiry = timeNow - solarisTimeDelta%1600000 + 400000
    #print([solarisTime,solarisExpiry])
    solarisCard = [{
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"福尔图纳/奥布山谷环境为:\n - **{solarisTime}**"
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": solarisExpiry
        },
        {"type": "divider"}]


    # Zariman: Need calculate/ 1.5 hours cycle
    # 1700042131982 Grineer start
    zarimanStatus = {0:"Grineer",1:"Corpus"}
    zarimanTimeDelta = timeNow - 1700042131982
    zarimanStatusType = int(zarimanTimeDelta/9000000)%2
    zarimanTime = zarimanStatus[zarimanStatusType]
    zarimanExpiry = dayEnd
    zarimanCard = [{
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"扎里曼号入侵状态为:\n - **{zarimanTime}**"
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": zarimanExpiry
        },
        {"type": "divider"}]

    # Duviri: Need mod. Done.
    # 1700006400000 joy start
    # 1700013600000 joy ends, anger start
    # 1700020800000 anger ends, envy start
    #  Joy -> Anger -> Envy -> Sorrow -> Fear
    duviriMoods = {0:"喜悦",1:"愤怒",2:"嫉妒",3:"悲伤",4:"恐惧",5:"喜悦"}
    duviriTimeDelta = timeNow - 1700006400000
    duviriMoodType = int(duviriTimeDelta/7200000)%5
    duviriExpiry = 7200000- duviriTimeDelta%7200000 + timeNow
    duviriTime = duviriMoods[duviriMoodType]
    duviriNextMood = duviriMoods[duviriMoodType+1]
    duviriCard = [{
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"双衍王境复眠螺旋为:\n - **{duviriTime}**\n - 下一个螺旋为: **{duviriNextMood}**"
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": duviriExpiry
        }]

    cycleCard[0]['modules'].extend(cytusCard+solarisCard+zarimanCard+duviriCard)
    return cycleCard