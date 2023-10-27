#api:https://10o.io/arbitrations.json
import sys
import os
import json
import requests
import datetime
from khl.card import CardMessage
sys.path.append(os.path.join(os.getcwd()))
from function.get_solnode_info import solNode
from function.time2stamp import get_time_stamp

# with open('config/config.json', 'r', encoding='utf-8') as f1,\
#     open('translate/translate_dict.json', 'r', encoding='utf-8') as f3:

#     config = json.load(f1)
#     translateCatagory = json.load(f3)

# platform = config['platform']


def arbitration():
    #arbitrationStats = requests.get(f"https://api.warframestat.us/{platform}/en/arbitration")
    with open('config/config.json','r',encoding='utf-8') as f:
        config = json.load(f)
        pushArbitration = config['arbitrations']
    
    try:
        arbitrationStats = requests.get("https://10o.io/arbitrations.json",timeout=(5,5))
    except:
        print("retry...")
        arbitration()
    arbitration_dict = arbitrationStats.json()
    print("[ init ] Arbitration. Status code:",arbitrationStats.status_code)
    solnode_info = solNode(arbitration_dict[0]['solnode'])
    try:
        _ = pushArbitration.index(arbitration_dict[0]['solnode'])
        push = 1
    except:
        push = 0
    #获取并翻译节点位置
    if (arbitration_dict[0]['solnode'] == "SolNode450"):
        arbitrationContent = "Tyana Pass 火星 - Corpus\n - 镜像防御"
    else:
        arbitrationContent =  "仲裁更新了:\n\n"\
    + solnode_info['name'] + " "\
    + solnode_info['systemName'] + " - "\
    + solnode_info['faction'] + "\n - "\
    + solnode_info['type']
    #处理卡片消息
    arbitrationRefreshTime = get_time_stamp(arbitration_dict[0]['end']) * 1000
    nowtime = datetime.datetime.now(datetime.timezone.utc).timestamp()*1000
    arbitrationRefreshTime = nowtime - nowtime%3600000 +3600000
    arbitrationCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": arbitrationContent
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": arbitrationRefreshTime
        }
        ]
    }
    #print(arbitrationCard)
    #响应并回复
    cm = CardMessage(arbitrationCard)
    return cm,push
# print(arbitration()[0][0]['theme'])
print(arbitration())