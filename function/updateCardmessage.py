import json
from khl import Bot

with open('config/config.json', 'r', encoding='utf-8') as f1:
    config = json.load(f1)
bot = Bot(token=config['token'])

async def upd_card(msg_id: str, content,target_id = ''):
    content = json.dumps(content)
    data = {'msg_id': msg_id, 'content': content}
    if target_id != '':
        data['temp_target_id'] = target_id
    result = await bot.client.gate.request('POST', 'message/update', data =data)
    return result