import json
import os
import sys
import datetime

sys.path.append(os.path.join(os.getcwd()))
from function.get_solnode_info import solNode
print("[ init ] Archon.")

#func
def archon():
    with open("content/worldState.json",'r',encoding='utf-8') as f:
            worldState_dict=json.load(f)
    with open("content/extra/SolNode.json",'r',encoding='utf-8') as f:
            node_dict=json.load(f)
    with open("translate/sortie_tags.json",'r',encoding='utf-8') as f:
            tag_dict=json.load(f)

    print(f"{datetime.datetime.now()} [Archon] Done.")
    archon_dict = worldState_dict['LiteSorties'][0]

    archonBoss = tag_dict['Bosses'].get(archon_dict['Boss'],archon_dict['Boss'])
    archonExpiry = int(archon_dict['Expiry']['$date']['$numberLong'])

    archonMission_node_info = []
    archonMission_type_info = []

    for i in range(3):
        archonMission_node_info.append(solNode(archon_dict['Missions'][i]['node']))
        archonMission_type = [obj for obj in node_dict['missionTypes'] if obj['missionType']==archon_dict['Missions'][i]['missionType']]
        archonMission_type_info.append(archonMission_type[0]['type'])

    archonCard = [{
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"执刑官猎杀信息:\n[{archonBoss}]"
            }
        }]
        }]

    num_dict = {"0":"任务一:","1":"任务二:","2":"任务三:"}
    for i in range(3):
        archonContent = f"{num_dict[f'{i}']} {archonMission_node_info[i]['name']} - {archonMission_node_info[i]['systemName']}\n - {archonMission_type_info[i]}"
        archonCard[0]['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": archonContent
            }
        })
    archonCard[0]['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": archonExpiry
        })
    return archonCard