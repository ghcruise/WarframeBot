import requests
import json
import re
from fuzzywuzzy import fuzz
from khl.card import CardMessage

with open("translate/wiki_translations.json",'r',encoding='utf-8')as f:
    weapenTranslate = json.load(f)
# itemName = "DualToxocyst"
# result = [obj for obj in weapenTranslate['ExportWeapons'] if (fuzz.token_set_ratio(itemName,obj['description'])>90)]
# print(result)

def endlessCircuit():
    # worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    # worldState_dict = worldState.json()
    with open("content/worldState.json",'r',encoding='utf-8') as f:
        worldState_dict=json.load(f)
    # print("[ init ] EXC. Status Code:",worldState.status_code)
    EXC_expiry = worldState_dict['LiteSorties'][0]['Expiry']['$date']['$numberLong']
    EXC_dict = worldState_dict['EndlessXpChoices']
    EXC_normal = EXC_dict[0]['Choices']
    EXC_hard = EXC_dict[1]['Choices']
    # print(EXC_normal)
    # print(EXC_hard)
    # print(EXC_expiry)


    EXC_normal_content = f"本周无尽回廊可选战甲:\n**{EXC_normal[0]}**"
    i = 1
    while i<len(EXC_normal):
        EXC_normal_content += f",**{EXC_normal[i]}**"
        i += 1

    #print(EXC_normal_content)

    EXC_hard_content = f"本周钢铁回廊可选灵化之源:\n"
    i = 0
    while i<len(EXC_hard):
        itemName = str.lstrip(re.sub(r'([A-Z]+[^A-Z])',r' \1',EXC_hard[i])).replace('AND','&')
        EXC_hard_content += f"**{weapenTranslate['Text'].get(itemName,itemName)}**,"
        # result = [obj for obj in weapenTranslate['ExportWeapons'] if (fuzz.token_set_ratio(itemName,obj['description'])==100)]
        # if i == 0:
        #     EXC_hard_content += f"**{result[0]['name']}**"
        # else:
        #     EXC_hard_content += f",**{result[0]['name'].replace(' Prime','')}**"
        i += 1
    #print(EXC_hard_content)
    EXC_hard_content=EXC_hard_content[:-1]

    circuitCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": EXC_normal_content
            }
        },
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": EXC_hard_content
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": EXC_expiry
        }
        ]
    }
    cm = CardMessage(circuitCard)
    return cm

# print(endlessCircuit())
