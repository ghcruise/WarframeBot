import subprocess

p=subprocess.Popen(["python3","content/get_api_json.py"])
p.wait()

m=subprocess.Popen(["python3","main.py"])