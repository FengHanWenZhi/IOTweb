from IOTEWMPApp.models import *


struct_data = {
    "type":"TemperatureSensor",
    "num": "AXED23R",
    "name":"温度1",
    "updata":80,
    "downdata":-10,
    "finish_updata_flag":True,
}

def receive_data(struct_data):
    flag = struct_data['finish_updata_flag']

    if flag == True:
        sensorNum = struct_data['num']
        sensorName = struct_data['name']
        sensorUpdata = struct_data['updata']
        sensorDowndata = struct_data['downdata']

        type = struct_data['type']
        if type == "TemperatureSensor":
            aSensor = TemperatureSensor(num=sensorNum,name=sensorName, deviceStatus=True, temperature=50,
                                        updata=sensorUpdata,downdata=sensorDowndata)
            aSensor.save()
        elif type == "FloodlightSensor":
            aSensor = FloodlightSensor(num=sensorNum, name=sensorName, deviceStatus=True, floodlight=350.64,
                                        updata=sensorUpdata, downdata=sensorDowndata)
            aSensor.save()
        else:
            aSensor = HumiditySensor(num=sensorNum, name=sensorName, deviceStatus=True, humidity=50.64,
                                        updata=sensorUpdata, downdata=sensorDowndata)
            aSensor.save()


def receiveExe():
    struct_data = {
        "type": "TemperatureSensor",
        "num": "AXED23R",
        "name": "温度1",
        "updata": 80,
        "downdata": -10,
        "finish_updata_flag": True,
    }
    receive_data(struct_data)


