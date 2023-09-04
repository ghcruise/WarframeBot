import requests
import sys
import os
import time
import json
from khl.card import CardMessage

sys.path.append(os.path.join(os.getcwd()))
from function.translate_uni2zh import uni2zh

with open('translate/translate_dict.json', 'r', encoding='utf-8') as f1:
    translateDict = json.load(f1)
print("[ init ] VoidTrader.")
def voidTrader():
    #UTC+8
    #local_time = time.time() * 1000 + 3600 * 8
    worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    worldState_dict = worldState.json()
    voidTrader_raw = worldState_dict['VoidTraders']
    startTime = voidTrader_raw[0]['Activation']['$date']['$numberLong']
    # local_time = worldState_dict['Time'] * 1000
    # print(f"start:{startTime}")
    # print(f"local:{local_time}")
    
    # if (local_time < float(startTime)):
    #     baroNode = translateDict[voidTrader_raw[0]['Node'].replace("HUB","")]
    #     baroContent = "下次虚空商人到达 : "+baroNode+"中继站"
    #     baroCard = {
    #     "type": "card",
    #     "theme": "success",
    #     "size": "lg",
    #     "modules": [
    #     {
    #         "type": "section",
    #         "text": {
    #         "type": "plain-text",
    #         "content": baroContent
    #         }
    #     },
    #     {
    #     "type": "countdown",
    #     "mode": "day",
    #     "endTime": startTime
    #     }
    #     ]
    # }
    #     cm = CardMessage(baroCard)
    #     return cm
    try:
        baroItem = voidTrader_raw[0]['Manifest']
        totalItem = len(baroItem)

        itemName = []
        primePrice = []
        regularPrice = []
        i = 0
        while i < totalItem:
            itemUName = baroItem[i]['ItemType'].replace("/Lotus/StoreItems/","/Lotus/")
            itemName.append(uni2zh(itemUName))
            primePrice.append(baroItem[i]['PrimePrice'])
            regularPrice.append(baroItem[i]['RegularPrice'])
            i += 1

        baroCard = {
                    "type": "card",
                    "theme": "success",
                    "size": "lg",
                    "modules": [
                    ]
                }

        j = 0
        while j < totalItem:
            baroContent = itemName[j]+"\n - "+"(font)"+str(primePrice[j])+"(font)[warning]"+"杜卡德 "+str("{:,}".format(regularPrice[j]))+"现金"
            baroCard['modules'].append({
                    "type": "section",
                    "text": {
                    "type": "kmarkdown",
                    "content": baroContent
                    }})
            j += 1
        print("Baro arrived!")
    except:
        baroNode = translateDict[voidTrader_raw[0]['Node'].replace("HUB","")]
        baroContent = "下次虚空商人到达 : "+baroNode+"中继站"
        baroCard = {
        "type": "card",
        "theme": "success",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "plain-text",
            "content": baroContent
            }
        },
        {
        "type": "countdown",
        "mode": "day",
        "endTime": startTime
        }]}
        print("Baro is still in void.")
            
    cm = CardMessage(baroCard)
    return cm
#print(voidTrader())