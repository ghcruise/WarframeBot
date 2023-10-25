import os
import sys
import json
import requests
from khl.card import CardMessage

sys.path.append(os.path.join(os.getcwd()))
# from function.time2stamp import get_time_stamp
from function.translate_uni2zh import uni2zh


# with open('config/config.json', 'r', encoding='utf-8') as f1,\
#     open('translate/translate_dict.json', 'r', encoding='utf-8') as f2:
#     config = json.load(f1)
#     translateDict = json.load(f2)

# platform = config['platform']

def dailyDeal():
    # darvo_raw = requests.get(f"https://api.warframestat.us/{platform}/en/dailyDeals")
    worldState = requests.get("http://content.warframe.com/dynamic/worldState.php")
    worldState_dict = worldState.json()
    print("[ init ] Darvo. Status Code:",worldState.status_code)
    darvo_dict = worldState_dict['DailyDeals']
    if (darvo_dict == []):
        return None
    else:
      darvo_item = uni2zh(darvo_dict[0]['StoreItem'].replace('StoreItems/',''))
      item_originalPrice = darvo_dict[0]['OriginalPrice']
      item_salePrice = darvo_dict[0]['SalePrice']
      item_total = darvo_dict[0]['AmountTotal']
      item_sold = darvo_dict[0]['AmountSold']
      item_remain = item_total - item_sold
      item_discount = darvo_dict[0]['Discount']
      item_expiry = darvo_dict[0]['Expiry']['$date']['$numberLong']
      
      cardContent1 = f"[{darvo_item} -{item_discount}%off] 库存:{item_remain}/{item_total}"
      cardContent2 = f"原价 {item_originalPrice}白金  现价 {item_salePrice}白金"

      darvoCard = {
          "type": "card",
          "theme": "success",
          "size": "lg",
          "modules": [
          {
              "type": "section",
              "text": {
              "type": "plain-text",
              "content": cardContent1
          }
        },
        {
              "type": "section",
              "text": {
              "type": "plain-text",
              "content": cardContent2
          }
        },
        
        {
          "type": "countdown",
          "mode": "day",
          "endTime": item_expiry
        }
      ]
      }
      cm = CardMessage(darvoCard)
      return cm,darvo_item,item_discount

print(dailyDeal())
