import json

with open("content/extra/SolNode.json",'r',encoding='utf-8') as f0:
    sol_info = json.load(f0)

with open("content/extra/CrewBattleNode.json",'r',encoding='utf-8') as f1:
    crew_info = json.load(f1)

with open("content/ExportRegions_zh.json",'r',encoding='utf-8') as f2:
    sol_dict = json.load(f2)

def solNode(nodeName):
    nodeInfo = [obj for obj in sol_dict['ExportRegions'] if obj['uniqueName']==nodeName]
    if not nodeInfo:
        try:
            crewNode = crew_info[f'{nodeName}']
            nodeInfo=[{'uniqueName':f'{nodeName}'}]
            nodeInfo[0]['name'] = crewNode['value']
            nodeInfo[0]['type'] = crewNode['type']
            nodeInfo[0]['systemName'] = ""
            nodeInfo[0]['Region'] = crewNode['systemIndex']
            nodeInfo[0]['faction'] = crewNode['enemy']
            return nodeInfo[0]
        except:
            nodeInfo=[{'uniqueName':f'{nodeName}'}]
            nodeInfo[0]['name']= nodeName
            nodeInfo[0]['systemName'] = ""
            return nodeInfo[0]
    else:
        #print(nodeInfo)
        #print(sol_info['missionType'])
        nodeMissionType = [obj for obj in sol_info['missionTypes'] if obj['missionIndex']==nodeInfo[0]['missionIndex']]
        #print(nodeMissionType)
        nodeFaction = [obj for obj in sol_info['missionFactions'] if obj['factionIndex']==nodeInfo[0]['factionIndex']]
        nodeInfo[0]['type']=nodeMissionType[0]['type']
        nodeInfo[0]['faction']=nodeFaction[0]['faction']
        return nodeInfo[0]

# print(solNode("EventNode1"))
# print(solNode("SolNode747"))