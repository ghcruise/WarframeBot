# ZJM----- uid 16730771
import json
from bilibili_api import Credential
from bilibili_api import dynamic

async def get_news(i:int=0):
    #get sessdata
    with open("config/config.json",'r',encoding='utf-8')as f:
        sessdata = json.load(f)['sessdata']
    token = Credential(sessdata)

    #get id
    with open("api_module/news/test.json")as f:
        idBox = json.load(f)

    #get dynamic
    t = await dynamic.get_dynamic_page_info(credential=token,host_mid=16730771)

    d= await dynamic.Dynamic.get_info(t[i])
    try:
        d_title = d['item']['modules']['module_dynamic']['major']['opus']['title']
        d_text = d['item']['modules']['module_dynamic']['major']['opus']['summary']['text']
    except:
        d_title = None
        d_text = None
    d_id = d['item']['id_str']
    # idBox=[]
    # print(f"\n{d_id}:")
    if d_title == None:
        text = d_text
        # print(f"{d_text}\nhttps://www.bilibili.com/opus/{d_id}")
    else:
        text = d_title
        # print(f"{d_title}\nhttps://www.bilibili.com/opus/{d_id}")
    link = f"https://www.bilibili.com/opus/{d_id}"
    idBox.append(d_id)
    idBox=list(set(idBox))
    with open("api_module/news/test.json","w",encoding='utf-8') as f:
        json.dump(idBox,f,ensure_ascii=False,indent=4)
    
    newsCard= [
    {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
            {
                "type": "section",
                "text": {
                "type": "kmarkdown",
                "content": "收到一份订阅动态："
                }
            },
            {
                "type": "section",
                "text": {
                "type": "kmarkdown",
                "content": f"{text}"
                }
            },
            {
                "type": "section",
                "text": {
                "type": "kmarkdown",
                "content": f"[查看动态详情]({link})"
                }
            }
        ]
    }]
    return newsCard,text,link