import os
import sys
import time
import json
import logging
from khl import Bot , Message ,EventTypes ,Event

sys.path.append(os.path.join(os.getcwd(), 'api_module'))
from content.get_worldState import getWorldState
from function.updateCardmessage import upd_card
from api_module.arbitration import arbitration
from api_module.sortie import sortie
from api_module.archonHunt import archon
from api_module.darvo import dailyDeal
from api_module.voidFissures import getFissures
from api_module.nightWave import nightWave
from api_module.voidTrader import voidTrader
from api_module.warframemarket.wm import wmSearch
from api_module.pushNotification.eidolon import eidolonHunter
from api_module.duviriEndless import endlessCircuit
from api_module.invasion import invasion
from api_module.pushNotification.invasionSort import invasionPush
from api_module.event import event
from api_module.alert import alert
from api_module.pushNotification.fissureSort import fissurePush
from api_module.cycle import get_cycle


with open('config/config.json', 'r', encoding='utf-8') as f1,\
    open('translate/translate_dict.json', 'r', encoding='utf-8') as f2,\
    open('translate/translate_catagory.json', 'r', encoding='utf-8') as f3:

    config = json.load(f1)
    translateDict = json.load(f2)
    translateCatagory = json.load(f3)


bot = Bot(token=config['token'])
platform = config['platform']
channelID = config['notifcationChannelID']
timestamp = int(time.time())
timeDelta = 8

card = [
    {
        "type": "card",
        "theme": "info",
        "size": "lg",
        "modules": [
        {
            "type": "section",
            "text": {
            "type": "kmarkdown",
            "content": "正在获取信息中..."
            }
        }
        ]
    }
    ]

#获取世界状态
@bot.task.add_cron(hour='*', minute="0/1")
async def update_worldState():
    getWorldState()

#五大平原状态
@bot.command(name='平原',prefixes=[''])
async def command_cetus(msg:Message):
    # cm = get_cycle()
    # await msg.ctx.channel.send(cm)
    temp = await msg.ctx.channel.send(card)
    await upd_card(temp['msg_id'],get_cycle(),)

#三傻推送
cm_eidolon_sub = eidolonHunter()
@bot.task.add_cron(hour='*', minute="1/5")
async def command_eidonlon_sub():
            global cm_eidolon_sub
            cm2 = eidolonHunter()
            if ((cm2[1]==1) and (cm_eidolon_sub[1]==0)):
                cm_eidolon_sub = cm2
                ch = await bot.client.fetch_public_channel(channelID)
                await bot.send(ch,cm2[0])
            else:
                cm_eidolon_sub = cm2
                print("no_eidolon")

#仲裁
@bot.command(name='仲裁',prefixes=[''])
async def command_arbitration(msg:Message):
    cm = arbitration()[0]
    await msg.ctx.channel.send(cm)

#仲裁推送
# cm_arbtration_sub = arbitration()[0]
# @bot.task.add_cron(hour='0/1', minute="1-5",second="30")
# async def command_arbitration_sub():
#             global cm_arbtration_sub
#             cm2 = arbitration()[0]
#             if (cm2 == cm_arbtration_sub):
#                 cm_arbtration_sub = cm2
#                 print("same_arb")
#             else:
#                 cm_arbtration_sub = cm2
#                 ch = await bot.client.fetch_public_channel(channelID)
#                 await bot.send(ch,cm2)

#仲裁好图推送
arbitrationPush = 0
@bot.task.add_cron(hour='0/1', minute="0-3",second="50")
async def command_arbitration_push():
            global arbitrationPush
            cm = arbitration()
            if (cm[1] == 0):
                arbitrationPush = 0
                print("arb is no value.")
            elif arbitrationPush==0:
                arbitrationPush=1
                cm[0][0]['theme']="danger"
                ch = await bot.client.fetch_public_channel(channelID)
                await bot.send(ch,cm[0])

#突击
@bot.command(name='突击',prefixes=[''])
async def command_sortie(msg:Message):
    cm = sortie()
    await msg.ctx.channel.send(cm)

#突击推送
cm_sortie_sub = sortie()
@bot.task.add_cron(hour=f"{(16+timeDelta)%24}-{(18+timeDelta)%24}", minute="2-4")
async def command_sortie_sub():
            global cm_sortie_sub
            cm2 = sortie()
            if (cm2 == cm_sortie_sub):
                print("same_sortie")
            else:
                cm_sortie_sub = cm2
                ch = await bot.client.fetch_public_channel(channelID)
                await bot.send(ch,cm2)

#执刑官猎杀
@bot.command(name='猎杀',prefixes=[''])
async def command_archon(msg:Message):
    cm = archon()
    await msg.ctx.channel.send(cm)

#猎杀推送
cm_archon_sub = None
@bot.task.add_cron(day_of_week="MON", hour=f"{(0+timeDelta)%24}", minute="3-5")
async def command_archon_sub():
            global cm_archon_sub
            cm2 = archon()
            if (cm2 == cm_archon_sub):
                print("same_archon")
            else:
                cm_archon_sub = cm2
                ch = await bot.client.fetch_public_channel(channelID)
                await bot.send(ch,cm2)

#每日特惠
@bot.command(name='特惠',prefixes=[''])
async def command_darvo(msg:Message):
    cm = dailyDeal()[0]
    await msg.ctx.channel.send(cm)

#每日特惠推送
cm_dailyDeal_sub = dailyDeal()
@bot.task.add_cron(hour='*', minute="0-2",second="10")
async def command_dailyDeal_sub():
            global cm_dailyDeal_sub
            cm2 = dailyDeal()
            if (cm2[1] == cm_dailyDeal_sub[1]):
                print("same_item")
            else:
                cm_dailyDeal_sub = cm2
                ch = await bot.client.fetch_public_channel(channelID)
                await bot.send(ch,cm2[0])

#虚空裂缝
@bot.command(name='裂缝',prefixes=[''])
async def command_voidfissureN(msg:Message):
    temp = await msg.ctx.channel.send(card)
    await upd_card(temp['msg_id'],getFissures()[0],)

#监听卡片消息点击:虚空裂缝
@bot.on_event(EventTypes.MESSAGE_BTN_CLICK)
async def event_voidfissure(_:Bot, e:Event):
    if (e.body['value']== "0" or e.body['value']=="1" or e.body['value']=="2"):
        await upd_card(e.body['msg_id'],getFissures()[int(e.body['value'])],)


#虚空裂缝
@bot.command(name='钢铁裂缝',prefixes=[''])
async def command_voidfissureH(msg:Message):
    temp = await msg.ctx.channel.send(card)
    await upd_card(temp['msg_id'],getFissures()[1],)
    
#虚空裂缝
@bot.command(name='风暴',prefixes=[''])
async def command_voidfissureS(msg:Message):
    cm = getFissures()[2]
    await msg.ctx.channel.send(cm)

#午夜电波
@bot.command(name='电波',prefixes=[''])
async def command_nightwave(msg:Message):
    temp = await msg.ctx.channel.send(card)
    await upd_card(temp['msg_id'],nightWave(),)
    # cm = nightWave()
    # await msg.ctx.channel.send(cm)

#奸商
@bot.command(name='奸商',prefixes=[''])
async def command_baro(msg:Message):
    cm = voidTrader()
    await msg.ctx.channel.send(cm)

#wm
@bot.command(name='wm',prefixes=[''])
async def command_wm(msg:Message,itemName:str="null",itemRank:int=0):
    cm = wmSearch(itemName,itemRank)
    await msg.ctx.channel.send(cm)

#回廊奖励
@bot.command(name='回廊',prefixes=[''])
async def command_circuit(msg:Message):
    cm = endlessCircuit()
    await msg.ctx.channel.send(cm)

#活动状态
@bot.command(name='活动',prefixes=[''])
async def command_event(msg:Message):
    cm = event()[0]
    await msg.ctx.channel.send(cm)

#警报
@bot.command(name='警报',prefixes=[''])
async def command_alert(msg:Message):
    cm = alert()
    await msg.ctx.channel.send(cm)

#入侵状态
@bot.command(name='入侵',prefixes=[''])
async def command_invsion(msg:Message):
    cm = invasion()[0]
    await msg.ctx.channel.send(cm)

#入侵推送
invasionData = []
@bot.task.add_cron(hour='*', minute="0/5",second="15")
async def command_invsionPush():
    global invasionData
    ch = await bot.client.fetch_public_channel(channelID)
    cm = invasionPush()
    for i in range(len(cm[0])):
        try:
            invasionData.index(cm[1][i])
        except:
            await bot.send(ch,cm[0][i])
    invasionData = cm[1]

#虚空裂缝推送
fissureID = []
@bot.task.add_cron(hour='*', minute="0/5",second="45")
async def command_fissurePush():
    global fissureID
    ch = await bot.client.fetch_public_channel(channelID)
    cm = fissurePush()
    for i in range(len(cm[0])):
        try:
            fissureID.index(cm[1][i])
        except:
            await bot.send(ch,cm[0][i])
    fissureID = cm[1]

logging.basicConfig(level='INFO')
bot.run()