import requests
import json
from khl.card import CardMessage
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

with open("api_module/warframemarket/wmItem.json",'r',encoding='utf-8')as f:
    translation = json.load(f)
#translator = translation['payload']['items']
def wmSearch(itemName,itemRank):
    #result = [obj for obj in translator if obj['item_name']==itemName]
    # try:
    #     item = result[0]['url_name']
    # except:
    #     item = itemName
    #     errorCard = {
    #          "type": "card",
    #         "theme": "danger",
    #         "size": "lg",
    #         "modules": [
    #         {
    #             "type": "section",
    #             "text": {
    #             "type": "kmarkdown",
    #             "content": f"没有找到\"**{itemName}**\"相关物品。\n请输入\"wm 物品名称\"进行查询\n带空格的物品用**英文引号**引起来就行"
    #             }
    #         }
    #         ]
    #     }
    #     cm_error = CardMessage(errorCard)
    
    result = [obj for obj in translation if (fuzz.token_set_ratio(itemName,obj['item_name'])>40)]
    result = process.extract(itemName,result,limit=5,scorer=fuzz.token_set_ratio)
    item = result[0][0]["url_name"]
    print(item)
    itemName = result[0][0]['item_name']
    print(itemName)
    print(itemRank)

    item_raw = requests.get(f"https://api.warframe.market/v1/items/{item}/orders?include=item")
    print(item_raw.status_code)
    # if item_raw.status_code == 404:
    #     return cm_error

    item_dict_raw = item_raw.json()
    
    #筛选在线玩家
    item_dict_online = [obj for obj in item_dict_raw['payload']['orders'] if (obj['user']['status']=="ingame" or obj['user']['status']=="online")]
    item_dict_offline = [obj for obj in item_dict_raw['payload']['orders'] if obj['user']['status']=="offline"]
    try:
        rank = item_dict_offline[0]['mod_rank']
        rank = 0
    except:
        rank = -1

    #价格排序，筛选卖家
    sorted_obj = sorted(item_dict_online, key=lambda x : x['platinum'], reverse=False)
    item_dict_online_sell = [obj for obj in sorted_obj if obj['order_type']=='sell']
    sorted_obj_1 = sorted(item_dict_offline, key=lambda x : x['platinum'], reverse=False)
    item_dict_offline_sell = [obj for obj in sorted_obj_1 if obj['order_type']=='sell']

    if rank == 0:
        modRank = itemRank
        item_dict_online_sell = [obj for obj in item_dict_online_sell if obj['mod_rank'] == modRank]
    print(item_dict_online_sell)
    name = []
    status = []
    reputation = []
    platinum = []
    quantity = []

    i = 0
    length = min(len(item_dict_online_sell),5)
    IDContent = "**游戏ID**"
    onlineStatus = "**在线状态**"
    price = "**单价(数量)**"
    while i < length:
        name.append(item_dict_online_sell[i]['user']['ingame_name'])
        reputation.append(item_dict_online_sell[i]['user']['reputation'])
        platinum.append(item_dict_online_sell[i]['platinum'])
        quantity.append(item_dict_online_sell[i]['quantity'])
        if item_dict_online_sell[i]['user']['status'] == "online":
            status.append("(font)在线(font)[success]")
        elif item_dict_online_sell[i]['user']['status'] == "ingame":
            status.append("(font)游戏中(font)[purple]")
        IDContent += '\nID:'+name[i]
        onlineStatus += '\n'+status[i]
        price += '\n'+str(platinum[i])+'白金 ('+str(quantity[i])+')'
        i += 1
    
    j = 0
    while length < 5:
        name.append(item_dict_offline_sell[j]['user']['ingame_name'])
        reputation.append(item_dict_offline_sell[j]['user']['reputation'])
        platinum.append(item_dict_offline_sell[j]['platinum'])
        quantity.append(item_dict_offline_sell[j]['quantity'])
        status.append("(font)离线(font)[danger]")
        IDContent += '\nID:'+name[j]
        onlineStatus += '\n'+status[j]
        price += '\n'+str(platinum[j])+'白金 ('+str(quantity[j])+')'
        length += 1
        j += 1

    print(IDContent)
    itemContent = "物品 " + itemName + " 的价格如下:"
    wmCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
        "type": "section",
        "text": {
          "type": "plain-text",
          "content": itemContent
        }
        },
        {
            "type": "section",
            "text": {
            "type": "paragraph",
            "cols": 3,
            "fields": [
                {
                "type": "kmarkdown",
                "content": IDContent
                },
                {
                "type": "kmarkdown",
                "content": onlineStatus
                },
                {
                "type": "kmarkdown",
                "content": price
                }
            ]
            }
        }
        ]
    }
    cm = CardMessage(wmCard)
    return cm