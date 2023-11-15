# 1700020800,000 anger ends, envy start
#  Joy -> Anger -> Envy -> Sorrow ->Fear
import json
import sys
import os
import datetime
sys.path.append(os.path.join(os.getcwd()))

timeNow = int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000)
print(timeNow)

#func
with open("content/worldState.json",'r',encoding='utf-8') as f:
    worldState_dict=json.load(f)

state_info = [obj for obj in worldState_dict['SyndicateMissions'] if obj['Tag']=="CetusSyndicate"]
dayStart = int(state_info[0]['Activation']['$date']['$numberLong'])
dayEnd = int(state_info[0]['Expiry']['$date']['$numberLong'])
print([dayStart,dayEnd])

# Cytus & Entrati : No paradox
dayDuration = dayEnd - dayStart
timeDelta = timeNow - dayStart
cytusDaytime = 100 * 60 * 1000
print([timeDelta,cytusDaytime,dayDuration])
if timeDelta < 6000000:
    cytusTime = "白天"
    entratiTime = "Fass"
else:
    cytusTime = "夜晚"
    entratiTime = "Vome"

# Solaris : Need mod
# A cycle: 26m 40s
# Warm 6m 40s
# Cold 20m

