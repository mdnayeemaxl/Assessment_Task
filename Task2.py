import os
import json
path=r"C:\Users\Md Nayeem\Desktop\Task\New folder\data"
l = os.listdir(path)
newDict={"description": "","tags": [],"size": {"height": 720,"width": 1280},"objects": []}

for fi in l:
    fpath=path+'\\'+fi
    with open( fpath,"r") as f:
        data = json.load(f)
    objList = data['objects']
    for i in objList:
        if(i["classTitle"]=='Vehicle'):
            i["classTitle"]="car"
        elif(i["classTitle"]=="License Plate"):
            i["classTitle"] = "number"
        newDict["objects"].append(i)

with open('test.json',"w") as fs:
    json.dump(newDict,fs,indent=4)
