import os
import json
path=r"C:\Users\Md Nayeem\Desktop\Task\New folder\data"
l = os.listdir(path)

for fi in l:
    fpath=path+'\\'+fi
    with open( fpath,"r") as f:
        data = json.load(f)


    formatedData =[]
    formateStyle =  {
            "dataset_name": "pos_10492.png.json",
            "image_link": "",
            "annotation_type": "image",
            "annotation_objects": {
                "vehicle": {
                    "presence": 0,
                    "bbox": []
                },
                "license_plate": {
                    "presence": 0,
                    "bbox": []
                }
            },
            "annotation_attributes": {
                "vehicle": {
                    "Type": None,
                    "Pose": None,
                    "Model": None,
                    "Make": None,
                    "Color":None
                },
                "license_plate": {
                    "Difficulty Score":None,
                    "value": None,
                    "Occlusion":None
                }
            }
        }



    objList = data['objects']
    for i in objList:
        if(i["classTitle"]=='Vehicle'):
            formateStyle["annotation_attributes"]["vehicle"]["Type"] = i['tags'][0]["value"]
            formateStyle["annotation_attributes"]["vehicle"]["Pose"] = i['tags'][1]["value"]
            formateStyle["annotation_attributes"]["vehicle"]["Model"] = i['tags'][2]["value"]
            formateStyle["annotation_attributes"]["vehicle"]["Make"] = i['tags'][3]["value"]
            formateStyle["annotation_attributes"]["vehicle"]["Color"] = i['tags'][4]["value"]
            points=i["points"]["exterior"]
            p=[]
            for j in points:
                p+=j
            formateStyle["annotation_objects"]["vehicle"]["bbox"] =p
            formateStyle["annotation_objects"]["vehicle"]["presence"] =1
        elif(i["classTitle"]=='License Plate'):
            formateStyle["annotation_attributes"]["license_plate"]["Difficulty Score"]=i['tags'][0]["value"]
            formateStyle["annotation_attributes"]["license_plate"]["value"] =i['tags'][1]["value"]
            try:
                occlusion=i['tags'][2]["value"]
            except:
                Occlusion=0
            formateStyle["annotation_attributes"]["license_plate"]["Occlusion"] = Occlusion
            points = i["points"]["exterior"]
            q=[]
            for k in points:
                q+=k
            formateStyle["annotation_objects"]["license_plate"]["bbox"] =q
            formateStyle["annotation_objects"]["license_plate"]["presence"] =1




    fileName = "formatted_"+fi
    with open(fileName,"w") as fs:
        json.dump(formateStyle,fs,indent=4)
