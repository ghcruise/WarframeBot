import requests
import json
import os
import sys
from khl.card import CardMessage

sys.path.append(os.path.join(os.getcwd()))
from function.translateNode import translateNode
from function.time2stamp import get_time_stamp

with open('config/config.json', 'r', encoding='utf-8') as f1,\
    open('translate/translate_dict.json', 'r', encoding='utf-8') as f2,\
    open('translate/translate_catagory.json', 'r', encoding='utf-8') as f3,\
    open('translate/translate_sortie.json', 'r', encoding='utf-8') as f4:

    config = json.load(f1)
    translateDict = json.load(f2)
    teanslateModifier = json.load(f4)

platform = config['platform']

def sortie():
  sortie_raw = requests.get(f"https://api.warframestat.us/{platform}/en/sortie/")
  print("[ init ] Sortie. Status code:",sortie_raw.status_code)
  sortie_dict = sortie_raw.json()

  sortieBoss = translateDict.get(sortie_dict['boss'],sortie_dict['boss'])
  sortieFaction = sortie_dict['faction']
  sortieExpiry = get_time_stamp(sortie_dict['expiry']) * 1000

  sortieMission1 = sortie_dict['variants'][0]
  sortieMission2 = sortie_dict['variants'][1]
  sortieMission3 = sortie_dict['variants'][2]

  sortieMission1_type = translateDict[sortieMission1['missionType']]
  sortieMission2_type = translateDict[sortieMission2['missionType']]
  sortieMission3_type = translateDict[sortieMission3['missionType']]

  sortieMission1_node = translateNode(sortieMission1['node'])
  sortieMission2_node = translateNode(sortieMission2['node'])
  sortieMission3_node = translateNode(sortieMission3['node'])

  sortieMission1_modifier = teanslateModifier.get(sortieMission1['modifier'],sortieMission1['modifier'])
  sortieMission2_modifier = teanslateModifier.get(sortieMission2['modifier'],sortieMission2['modifier'])
  sortieMission3_modifier = teanslateModifier.get(sortieMission3['modifier'],sortieMission3['modifier'])

  #sortieContent = "["+sortieBoss+" - "+sortieFaction+"]\n突击一:"+sortieMission1_node+" "+sortieMission1_type+"\n -"+sortieMission1_modifier+"\n突击二:"+sortieMission2_node+" "+sortieMission2_type+"\n -"+sortieMission2_modifier+"\n突击三:"+sortieMission3_node+" "+sortieMission3_type+"\n -"+sortieMission3_modifier
  sortieContent0 = "突击更新了:\n"+"["+sortieBoss+" - "+sortieFaction+"]"
  sortieContent1 = "突击一:"+sortieMission1_node+" "+sortieMission1_type+"\n - "+sortieMission1_modifier
  sortieContent2 = "突击二:"+sortieMission2_node+" "+sortieMission2_type+"\n - "+sortieMission2_modifier
  sortieContent3 = "突击三:"+sortieMission3_node+" "+sortieMission3_type+"\n - "+sortieMission3_modifier
  sortieCard = {
    "type": "card",
    "theme": "success",
    "size": "lg",
    "modules": [
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": sortieContent0
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": sortieContent1
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": sortieContent2
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": sortieContent3
        }
      },

      {
        "type": "countdown",
        "mode": "day",
        "endTime": sortieExpiry
      }
    ]
  }
  cm = CardMessage(sortieCard)
  return cm