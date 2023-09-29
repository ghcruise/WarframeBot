<h1 align= "center">WarframeBot</h1>  

## Helios Prime  
基于python的Warframe KOOK机器人  
A Warframe notification bot based on python   
- [Helios Prime](#helios-prime)
- [查询功能-指令](#查询功能-指令)
- [进度-Todo](#进度-todo)
- [部署方法](#部署方法)
  - [Windows](#windows)
  - [Linux](#linux)


## 查询功能-指令 
- **突击**：查询每日突击，有推送
- **猎杀**：查询每周执行官猎杀，有推送  
- **仲裁**：查询当前仲裁任务,**有推送(谷防，谷拦)，支持自定义**
- **特惠**：查询Darvo的每日特惠，有推送
- **电波**：查询午夜电波，官方API~~有推送~~ Todo
- **裂缝**，**钢铁裂缝**，**风暴**：查询虚空裂缝(钢铁/九重天),**有推送(钢铁虚空生存,虚空歼灭捕获)，支持自定义** ~~感觉虚空风暴没啥必要,有需要就加~~  
- **奸商**：查询虚空商人物品，~~**官方API快人一步**~~
- **平原**：查询**希图斯**，**金星**，**火卫二**，**扎里曼**~~(这也是平原?)~~，**双衍王境**状态，夜灵平原天黑前有推送
- **回廊**：查询每周回廊可选物品，推送Todo
- **入侵**：查询入侵状态，有推送
- **活动**：查询当前活动，推送Todo
- **警报**：查询当前警报任务



## 进度-Todo
- [x] 每日突击 
    - [x] api来源warframestat.us
    - [ ] ~~使用官方API~~没必要
    - [x] 每日推送
- [x] 每周执刑官猎杀 
    - [x] api来源warframestat.us
    - [ ] ~~使用官方API~~没必要
    - [x] 每周推送  
- [x] Darvo每日特惠   
    - [x] ~~api来源warframestat.us~~
    - [x] 使用官方API 
    - [x] 更新推送
- [x] 午夜电波  
    - [x] ~~api来源warframestat.us~~
    - [x] 使用官方API
    - [ ] 推送~~看心情写~~
    - [ ] 查询奖励~~你上游戏看一下不就好了~~
- [x] 虚空裂缝/风暴-~~wfcd~~ 
    - [x] ~~api来源warframestat.us~~
    - [x] 虚空裂缝/风暴-**使用官方API**
    - [x] 完善SolNode查询(九重天部分)
    - [x] 试一下OKOK卡片消息交互 **可以在卡片中点击切换钢铁之路/虚空风暴的裂缝**
    - [x] 好缝推送 ~~隔壁居然要20R/月~~ **可以自定义推送列表**
- [x] 虚空商人
    - [x] 使用官方API  
- [x] 仲裁-第三方API  
    - [x] 更新推送
    - [x] 好图推送
    - [x] 完善SolNode查询
- [x] WarframeMarket查询 
    - [x] 模糊搜索
    - [ ] 紫卡搜索
- [x] 平原相关
    - [x] 夜灵平原/希图斯时间
        - [x] api来源warframestat.us
        - [x] 入夜推送
        - [x] ~~使用官方API~~ ~~没必要~~ 还是用了  
    - [x] 奥布山谷/福尔图纳状态
    - [x] 魔胎之境/殁世幽都状态
    - [x] 扎里曼号入侵状态
    - [x] 双衍王境复眠螺旋
- [x] 无尽回廊
    - [x] 普通回廊每周战甲
    - [x] 钢铁回廊每周灵化武器
    - [ ] 每周推送
- [ ] 警报
    - [x] 使用官方API
    - [ ] 推送
- [x] 入侵
    - [x] 使用官方API
    - [x] 推送
    - [x] 完善蓝图类的翻译内容
    - [x] 战舰&豺狼
- [ ] 活动
    - [x] 实现
    - [ ] 推送
 
## 部署方法  
打包下载``WarframeBot.git``
修改``config/config.json.example``中的内容  
填写平台``platform``(现阶段仅支持PC),KOOK机器人``TOKEN``和推送频道ID``notifcationChannelID``   
并重命名为``config.json``  
在Bot目录下运行
```
pip install -r requirements.txt  
```

### Windows
```
start.bat
```  
### Linux
```
run.sh
```