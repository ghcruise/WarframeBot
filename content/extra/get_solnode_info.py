import json

with open("content\ExportRegions_zh.json",'r',encoding='utf-8') as f:
    info_raw = json.load(f)

info = info_raw['ExportRegions']
mission_type = []
i = 0
while i < 100:
        type_num = [obj for obj in info if obj['missionIndex']==i]
        if not type_num:
              i += 1
              del type_num
        else:
            type_num_content = type_num[0]['missionIndex']
            #print(type_num_content)
            mission_type.append({"missionIndex":type_num_content,"missionType":"","type":""})
            i += 1
            del type_num

solNode_info = json.dumps(mission_type).replace('},','},\n')

with open("content\extra\SolNode_info.json",'w',encoding='utf-8') as f:
      f.write(solNode_info)