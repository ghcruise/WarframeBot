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

def archon():
  archonHunt_raw = requests.get(f"https://api.warframestat.us/{platform}/en/archonHunt/")
  print("[ init ] archon. Status code:",archonHunt_raw.status_code)
  archonHunt_dict = archonHunt_raw.json()

  archonBoss = translateDict.get(archonHunt_dict['boss'],archonHunt_dict['boss'])
  archonFaction = archonHunt_dict['faction']
  archonExpiry = get_time_stamp(archonHunt_dict['expiry']) * 1000

  archonMission1 = archonHunt_dict['missions'][0]
  archonMission2 = archonHunt_dict['missions'][1]
  archonMission3 = archonHunt_dict['missions'][2]

  archonMission1_type = translateDict[archonMission1['typeKey']]
  archonMission2_type = translateDict[archonMission2['typeKey']]
  archonMission3_type = translateDict[archonMission3['typeKey']]

  archonMission1_node = translateNode(archonMission1['node'])
  archonMission2_node = translateNode(archonMission2['node'])
  archonMission3_node = translateNode(archonMission3['node'])


  #sortieContent = "["+sortieBoss+" - "+sortieFaction+"]\n突击一:"+sortieMission1_node+" "+sortieMission1_type+"\n -"+sortieMission1_modifier+"\n突击二:"+sortieMission2_node+" "+sortieMission2_type+"\n -"+sortieMission2_modifier+"\n突击三:"+sortieMission3_node+" "+sortieMission3_type+"\n -"+sortieMission3_modifier
  archonContent0 = "["+archonBoss+" - "+translateDict[archonFaction]+"]"
  archonContent1 = "任务一:"+archonMission1_node+"\n - "+archonMission1_type
  archonContent2 = "任务二:"+archonMission2_node+"\n - "+archonMission2_type
  archonContent3 = "任务三:"+archonMission3_node+"\n - "+archonMission3_type
  archonCard = {
    "type": "card",
    "theme": "success",
    "size": "lg",
    "modules": [
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": archonContent0
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": archonContent1
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": archonContent2
        }
      },
      {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": archonContent3
        }
      },

      {
        "type": "countdown",
        "mode": "day",
        "endTime": archonExpiry
      }
    ]
  }
  cm = CardMessage(archonCard)
  return cm