import requests
import json

def clean_world_state(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_data = response.text

        parsed_data = json.loads(raw_data)
        print("JSON 数据解析成功！")
        return parsed_data
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
    return None

# URL
url = "http://content.warframe.com/dynamic/worldState.php"


def getWorldState():
    world_state_data = clean_world_state(url)

    if world_state_data:
        with open("content/worldState.json", "w", encoding="utf-8") as f:
            json.dump(world_state_data, f, indent=4, ensure_ascii=False)