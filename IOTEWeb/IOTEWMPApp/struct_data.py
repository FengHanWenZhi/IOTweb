from IOTEWMPApp.models import *
import time
import json

struct_data = {
    "type":"TemperatureSensor",
    "num": "AXED23R",
    "name":"温度1",
    "current_data":10,
    "updata":80,
    "downdata":-10,
    "finish_updata_flag":True,
}

def receive_data(struct_data):
    flag = struct_data['finish_updata_flag']

    if flag == True:
        sensorNum = struct_data['num']
        sensorName = struct_data['name']
        value = struct_data['current_data']
        sensorUpdata = struct_data['updata']
        sensorDowndata = struct_data['downdata']

        type = struct_data['type']
        if type == "TemperatureSensor":
            if len(TemperatureSensor.objects.filter(name=sensorName)) == 0 :
                aSensor = TemperatureSensor(num=sensorNum,name=sensorName, deviceStatus=False, temperature=value,
                                        updata=sensorUpdata,downdata=sensorDowndata)
                aSensor.save()
            else:
                oldSensor = TemperatureSensor.objects.get(name=sensorName)
                oldSensor.temperature = value
                oldSensor.updata = sensorUpdata
                oldSensor.downdata = sensorDowndata
                oldSensor.save(update_fields=['temperature'])
                oldSensor.save(update_fields=['updata'])
                oldSensor.save(update_fields=['downdata'])
        elif type == "FloodlightSensor":
            if len(FloodlightSensor.objects.filter(name=sensorName)) == 0:
                aSensor = FloodlightSensor(num=sensorNum, name=sensorName, deviceStatus=False, luminance=value,
                                        updata=sensorUpdata, downdata=sensorDowndata)
                aSensor.save()
            else:
                oldSensor = FloodlightSensor.objects.get(name=sensorName)
                oldSensor.luminance = value
                oldSensor.updata = sensorUpdata
                oldSensor.downdata = sensorDowndata
                oldSensor.save(update_fields=['luminance'])
                oldSensor.save(update_fields=['updata'])
                oldSensor.save(update_fields=['downdata'])
        else:
            if len(HumiditySensor.objects.filter(name=sensorName)) == 0:
                aSensor = HumiditySensor(num=sensorNum, name=sensorName, deviceStatus=False, humidity=value,
                                        updata=sensorUpdata, downdata=sensorDowndata)
                aSensor.save()
            else:
                oldSensor = HumiditySensor.objects.get(name=sensorName)
                oldSensor.humidity = value
                oldSensor.updata = sensorUpdata
                oldSensor.downdata = sensorDowndata
                oldSensor.save(update_fields=['humidity'])
                oldSensor.save(update_fields=['updata'])
                oldSensor.save(update_fields=['downdata'])
        struct_data["finish_updata_flag"] = False



# def receiveExe():
#     # struct_data = {
#     #     "type": "TemperatureSensor",
#     #     "num": "AXED23R",
#     #     "name": "温度1",
#     #     "updata": 80,
#     #     "downdata": -10,
#     #     "finish_updata_flag": True,
#     #}
#     receive_data(struct_data)


def rawinfo_to_structdata(c_to_s_data,structed_data):
    reversed_kv = {};  #反转键值对在字典中的顺序，前面的键值对放到后面，一会儿会从后面开始弹出；
    while c_to_s_data:
        k,v = c_to_s_data.popitem()
        t_item = {k:v}
        reversed_kv.update(t_item)
    while reversed_kv:
        print("rawinfo_to_structdata")
        time.sleep(0.01)
        if (structed_data["finish_updata_flag"] == False):
             head,item= reversed_kv.popitem()
             # print(head)
             # print(item)
             head_list = head.split("/")
             structed_data["type"] = head_list[0]
             structed_data["num"] = head_list[1]
             info_dir = json.loads(item)
             structed_data["name"] = info_dir["name"]
             struct_data["current_data"] = info_dir["attr"]["attr1"]
             structed_data["updata"] = info_dir["attr"]["attr2"]
             structed_data["downdata"] = info_dir["attr"]["attr3"]
             structed_data["finish_updata_flag"] = True
             print(structed_data)
        if (structed_data["finish_updata_flag"] == True):
            receive_data(structed_data)
            structed_data["finish_updata_flag"] = False

