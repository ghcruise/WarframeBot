import re
import json

with open("droptable/droptables.html",'r',encoding='utf-8')as f:
    droptable_h5 = f.read()
tables = re.findall(r'<table>(.*?)</table>', droptable_h5, re.DOTALL)
titles = re.findall(r'<h3 id="(.*?)">', droptable_h5, re.DOTALL)
# print(titles)
k=5
if k < 4:
    missionRwd = re.findall(r'(.*?)<tr class="blank-row"><td class="blank-row" colspan="2"></td></tr>', tables[k], re.DOTALL) + re.findall(r'<tr class="blank-row"><td class="blank-row" colspan="2"></td></tr>(.*?)<tr class="blank-row"><td class="blank-row" colspan="2"></td></tr>', tables[k], re.DOTALL)
elif k ==4:
    missionRwd = [tables[k]]
elif k>4:
    missionRwd = re.findall(r'<tr>(.*?)<td class="blank-row" colspan="3"></td></tr>', tables[k], re.DOTALL)
# print(missionRwd)
droptable = {}
droptable['drops']=[]
for j in range(len(missionRwd)):
    items = re.findall(r'<tr.*?>(.*?)</tr>', missionRwd[j], re.DOTALL)
    print(items)

    # print(len(items))
    test_result = []
    test_contrast = []
    for i in range(len(items)):
        test_title = re.findall(r'<th.*?>(.*?)</th>',items[i],re.DOTALL)
        test_item = re.findall(r'<td>(.*?)</td>',items[i],re.DOTALL)
        if len(test_title) == 0:
            test_result.append(test_item)
            test_contrast.append(0)
        else:
            test_result.append(test_title)
            test_contrast.append(1)
       
    # print(test_result)
    # print(test_contrast)
    miniTitle = ""
    for i in range(len(items)):
        if i == 0 :
            miniSource = test_result[0][0]
            print(miniSource)
        elif (test_contrast[i] == 1 and test_contrast[i-1] == 1 and test_contrast[i+1] == 0):
            # droptable[test_result[0][0]][test_result[i][0]]=[]
            miniTitle = test_result[i][0]
        elif test_contrast[i] == 0:
            droptable['drops'].append({"item":test_result[i][-2],"chance":test_result[i][-1],"rotation":miniTitle,"location":miniSource})

# print(droptable)
with open(f"droptable/droptables{k}.json",'w',encoding='utf-8')as f:
    json.dump(droptable,f,ensure_ascii=False,indent=4)

