import re

with open("droptable/droptables.html",'r',encoding='utf-8')as f:
    droptable_h5 = f.read()
tables = re.findall(r'<table>(.*?)</table>', droptable_h5, re.DOTALL)
titles = re.findall(r'<h3 id="(.*?)">', droptable_h5, re.DOTALL)
# print(titles)
missionRwd = re.findall(r'(.*?)<tr class="blank-row"><td class="blank-row" colspan="2"></td></tr>', tables[0], re.DOTALL) + re.findall(r'<tr class="blank-row"><td class="blank-row" colspan="2"></td></tr>(.*?)<tr class="blank-row"><td class="blank-row" colspan="2"></td></tr>', tables[0], re.DOTALL)
# print(missionRwd)
items = re.findall(r'<tr.*?>(.*?)</tr>', missionRwd[0], re.DOTALL)
# for i in range(items):
#     items[i].replace('</td><td>'," ")
print(items[2])