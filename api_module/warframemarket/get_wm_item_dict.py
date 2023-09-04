import requests
import json
from collections import ChainMap

requestHeaders = {
    "accept":"application/json",
    "Language":"zh-hans",
    "content-type":"application/json"
}

wmItem_raw = requests.get("https://api.warframe.market/v1/items",headers = requestHeaders)

with open("api_module/warframemarket/wmItem_zh.json",'w',encoding='utf-8') as f1:
    content = eval("u"+"'"+wmItem_raw.text+"'")
    f1.writelines(content)
del content
with open("api_module/warframemarket/wmItem_zh.json",'r',encoding='utf-8') as f2:
    content_txt = f2.readlines()
content_zh=[str.replace('},',"},\n").replace('],','],\n') for str in content_txt]
del content_txt
with open("api_module/warframemarket/wmItem_zh.json",'w',encoding='utf-8') as f3:
    f3.writelines(content_zh)
del content_zh

requestHeaders_en = {
    "accept":"application/json",
    "Language":"en",
    "content-type":"application/json"
}

wmItem_raw_en = requests.get("https://api.warframe.market/v1/items",headers = requestHeaders_en)

with open("api_module/warframemarket/wmItem_en.json",'w',encoding='utf-8') as f4:
    #content = eval("u"+"'"+wmItem_raw_en.text+"'")
    f4.writelines(wmItem_raw_en.text)
with open("api_module/warframemarket/wmItem_en.json",'r',encoding='utf-8') as f5:
    content_txt = f5.readlines()
content_en=[str.replace('},',"},\n").replace('],','],\n').replace('\"item_name\"','\"item_name_en\"') for str in content_txt]
del content_txt
with open("api_module/warframemarket/wmItem_en.json",'w',encoding='utf-8') as f6:
    f6.writelines(content_en)
del content_en

with open("api_module/warframemarket/wmItem_en.json",'r',encoding='utf-8') as f7:
    dict_en = json.load(f7)
with open("api_module/warframemarket/wmItem_zh.json",'r',encoding='utf-8') as f8:
    dict_zh = json.load(f8)

i = 0
dictLength = len(dict_zh['payload']['items'])
dict_all = []
while i < dictLength:
    dict_all.append({**dict_zh['payload']['items'][i],**dict_en['payload']['items'][i]})
    i += 1
# dict_all_str = json.dumps(dict_all)
dict_all_str = str(dict_all)
#dict_all_str = [str.replace('},',"},\n").replace('],','],\n') for str in dict_all_str]
with open("api_module/warframemarket/wmItem.json",'w',encoding='utf-8') as f9:
    f9.writelines(dict_all_str)


with open("api_module/warframemarket/wmItem.json",'r',encoding='utf-8') as f2:
    content_txt = f2.readlines()
content_zh=[str.replace('},',"},\n").replace('],','],\n').replace(' \'',' \"').replace('\':','\":').replace('{\'','{\"').replace('\'}','\"}').replace('\',','\",').replace('True','true').replace('False','false') for str in content_txt]
del content_txt
with open("api_module/warframemarket/wmItem.json",'w',encoding='utf-8') as f3:
    f3.writelines(content_zh)
del content_zh