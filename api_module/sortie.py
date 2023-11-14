import json
import os
import sys
import datetime

sys.path.append(os.path.join(os.getcwd()))
from function.get_solnode_info import solNode
print("[ init ] Sortie.")

#func
def sortie():
    with open("content/worldState.json",'r',encoding='utf-8') as f:
            worldState_dict=json.load(f)
    with open("content/extra/Solnode.json",'r',encoding='utf-8') as f:
            node_dict=json.load(f)
    with open("translate/sortie_tags.json",'r',encoding='utf-8') as f:
            tag_dict=json.load(f)

    print(f"{datetime.datetime.now()} [Sortie] Done.")
    sortie_dict = worldState_dict['Sorties'][0]

    sortieBoss = tag_dict['Bosses'].get(sortie_dict['Boss'],sortie_dict['Boss'])
    sortieExpiry = int(sortie_dict['Expiry']['$date']['$numberLong'])

    sortieMission_node_info = []
    sortieMission_type_info = []
    sortieMission_modifier_info = []
    for i in range(3):
        sortieMission_node_info.append(solNode(sortie_dict['Variants'][i]['node']))
        # sortieMission_node_info = solNode(sortie_dict['Variants'][1]['node'])
        # sortieMission_node_info = solNode(sortie_dict['Variants'][2]['node'])
        sortieMission_type = [obj for obj in node_dict['missionTypes'] if obj['missionType']==sortie_dict['Variants'][i]['missionType']]
        sortieMission_type_info.append(sortieMission_type[0]['type'])
        sortieMission_modifier_info.append(tag_dict['Modifier'].get(sortie_dict['Variants'][i]['modifierType'],sortie_dict['Variants'][i]['modifierType']))

    sortieCard = [{
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": f"突击信息:\n[{sortieBoss}]"
            }
        }]
        }]

    num_dict = {"0":"突击一:","1":"突击二:","2":"突击三:"}
    for i in range(3):
        sortieContent = f"{num_dict[f'{i}']} {sortieMission_node_info[i]['name']} - {sortieMission_node_info[i]['systemName']} {sortieMission_type_info[i]}\n - {sortieMission_modifier_info[i]}"
        sortieCard[0]['modules'].append({
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": sortieContent
            }
        })
    sortieCard[0]['modules'].append({
            "type": "countdown",
            "mode": "day",
            "endTime": sortieExpiry
        })
    return sortieCard