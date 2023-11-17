# ZJM----- uid 16730771
import json
from bilibili_api import sync
from bilibili_api import Credential
from bilibili_api import dynamic
with open("config/config.json",'r',encoding='utf-8')as f:
    sessdata = json.load(f)['sessdata']
token = Credential(sessdata)

t = sync(dynamic.get_dynamic_page_info(credential=token,host_mid=16730771))
# d = sync(dynamic.get_dynamic_page_UPs_info(token))
d= sync(dynamic.Dynamic.get_info(t[3]))
print(d['item']['modules']['module_dynamic']['major']['opus']['title'])
print(d['item']['modules']['module_dynamic']['major']['opus']['summary']['text'])
# with open("test.json","w",encoding='utf-8') as f:
#     json.dump(d,f,ensure_ascii=False,indent=4)