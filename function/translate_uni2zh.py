import json
import re
from fuzzywuzzy import fuzz

with open("content/ExportWeapons_zh.json",'r',encoding='utf-8') as f1:
    translateWeapons = json.load(f1)

with open("content/ExportWarframes_zh.json",'r',encoding='utf-8') as f2:
    translateWarframes = json.load(f2)

with open("content/ExportResources_zh.json",'r',encoding='utf-8') as f3:
    translateResources = json.load(f3)

with open("content/ExportFlavour_zh.json",'r',encoding='utf-8') as f3:
    translateFlavour = json.load(f3)

with open("content/ExportCustoms_zh.json",'r',encoding='utf-8') as f3:
    translateCustoms = json.load(f3)

with open("content/ExportUpgrades_zh.json",'r',encoding='utf-8') as f3:
    translateUpgrades = json.load(f3)

with open("content/ExportSortieRewards_zh.json",'r',encoding='utf-8') as f3:
    translateSortieRewards = json.load(f3)

with open("content/ExportRecipes_zh.json",'r',encoding='utf-8') as f3:
    findRecipesBlueprint = json.load(f3)

with open("content/ExportKeys_zh.json",'r',encoding='utf-8') as f3:
    translateKeys = json.load(f3)

with open("content/ExportRelicArcane_zh.json",'r',encoding='utf-8') as f3:
    translateRelicArcane = json.load(f3)

with open("content/ExportGear_zh.json",'r',encoding='utf-8') as f3:
    translateGear = json.load(f3)

with open("api_module/warframemarket/wmItem.json",'r',encoding='utf-8') as f4:
    translateWmItem = json.load(f4)

def uni2zh(ItemUname):
    result = [obj for obj in translateWeapons['ExportWeapons'] if obj['uniqueName']==ItemUname]
    if not result:
        result = [obj for obj in translateResources['ExportResources'] if obj['uniqueName']==ItemUname]
        if not result:
            result = [obj for obj in translateWarframes['ExportWarframes'] if obj['uniqueName']==ItemUname]
            if not result:
                result = [obj for obj in translateFlavour['ExportFlavour'] if obj['uniqueName']==ItemUname]
                if not result:
                    result = [obj for obj in translateCustoms['ExportCustoms'] if obj['uniqueName']==ItemUname]
                    if not result:
                        result = [obj for obj in translateUpgrades['ExportUpgrades'] if obj['uniqueName']==ItemUname]
                        if not result:
                            result = [obj for obj in translateSortieRewards['ExportOther'] if obj['uniqueName']==ItemUname]
                            if not result:
                                result = [obj for obj in translateKeys['ExportKeys'] if obj['uniqueName']==ItemUname]
                                if not result:
                                    result = [obj for obj in findRecipesBlueprint['ExportRecipes'] if obj['uniqueName']==ItemUname]                  
                                    if not result:
                                        result = [obj for obj in translateRelicArcane['ExportRelicArcane'] if obj['uniqueName']==ItemUname]
                                        if not result:
                                            result = [obj for obj in translateGear['ExportGear'] if obj['uniqueName']==ItemUname]
                                            if not result:
                                                fuckingName = ItemUname.split('/')[-1]
                                                print(fuckingName)
                                                fuckingItem = re.sub(r'([A-Z]+[^A-Z])',r' \1',fuckingName)
                                                #print(fuckingItem) 
                                                return str.lstrip(fuckingItem)
                                            else:
                                                return result[0]['name']
                                        else:
                                            return result[0]['name']                                    
                                    else:
                                        newUname = result[0]['resultType']
                                        itemName = f"{uni2zh(newUname)} 蓝图"
                                        return itemName
                                else:
                                    return result[0]['name']
                            else:
                                return result[0]['name']
                        else:
                            return result[0]['name']
                    else:
                        return result[0]['name']
                else:
                    return result[0]['name'].replace('/',',')
            else:
                return result[0]['name']
        else:
            return result[0]['name']
    else:
        return result[0]['name']
        