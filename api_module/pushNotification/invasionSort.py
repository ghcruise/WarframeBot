import json
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from api_module.invasion import invasion
print("[ init ] Push Invasions.")
def invasionPush():
    with open("config/config.json",'r',encoding='utf-8') as f:
        pushItem_all = json.load(f)

    #atkReward=3,defReward=6
    pushItem = pushItem_all['invasions']
    invasionList = invasion()[1]
    # print("invasionList:",invasionList)
    invasionIndex = []
    for i in range(len(pushItem)):
        for j , value in enumerate(invasionList[3]):
            if value == pushItem[i]:
                invasionIndex.append(j)
        for j , value in enumerate(invasionList[6]):
            if value == pushItem[i]:
                invasionIndex.append(j)
            # try: 
            #     invasionIndex.append(invasionList[3].index(pushItem[i]))
            # except:
            #     pass
            # try: 
            #     invasionIndex.append(invasionList[6].index(pushItem[i]))
            # except:
            #     pass
    invasionIndex = list(set(invasionIndex))
    # print(invasionIndex)

    sortedInvasionCard = []
    nodeInfo = []

    for i in invasionIndex:
        nodeInfo.append(invasionList[0][i])
        sortedInvasionCard.append([{
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
                    "content": f"**进攻方**\n{invasionList[1][i]}\n{invasionList[2][i]}%\n{invasionList[3][i]}"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"\n**{invasionList[0][i]}**\n**进度**\n**奖励**"
                    },
                    {
                    "type": "kmarkdown",
                    "content": f"**防守方**\n{invasionList[4][i]}\n{invasionList[5][i]}%\n{invasionList[6][i]}"
                    }
                ]
                }
            }
            ]
        }])
    #print(sortedInvasionCard[0])
    return sortedInvasionCard,nodeInfo
# print(invasionPush()[1])
