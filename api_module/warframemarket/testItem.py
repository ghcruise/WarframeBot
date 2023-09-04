import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
with open("api_module\warframemarket\wmItem.json",'r',encoding='utf-8')as f:
    translation = json.load(f)
itemName = "wisp一套"

translator = translation
result = [obj for obj in translator if (fuzz.token_set_ratio(itemName,obj['item_name'])>40)]
result = process.extract(itemName,result,limit=5,scorer=fuzz.token_set_ratio)
print(result)
item = result[0][0]["url_name"]
# try:
#     item = result[0]['url_name']
# except:
#     item = "null"
print(item)
