import time
import json

sensortype = "tmep"
sensorNum = "0000"
sensorName = "ahao"
current_value = 200
sensorUpdata = 300
sensorDowndata = 50
flag = True

struct_data = {
    "type":sensortype,
    "num": sensorNum,  #设备ID；
    "name":sensorName, #设备名称；
    # "current_data":current_value,
    "updata":sensorUpdata,
    "downdata":sensorDowndata,
    "finish_updata_flag":flag
}



def rawinfo_to_structdata(c_to_s_data,structed_data):
    reversed_kv = {};  #反转键值对在字典中的顺序，前面的键值对放到后面，一会儿会从后面开始弹出；
    while c_to_s_data:
        k,v = c_to_s_data.popitem()
        t_item = {k:v}
        reversed_kv.update(t_item)
    while reversed_kv:
             time.sleep(0.01)
        #if(structed_data["finish_updata_flag"] == False):
             head,item= reversed_kv.popitem()
             # print(head)
             # print(item)
             head_list = head.split("/")
             struct_data["type"] = head_list[0]
             struct_data["num"] = head_list[1]
             info_dir = json.loads(item)
             struct_data["name"] = info_dir["name"]
             # struct_data["current_data"] = info_dir["attr"]["attr1"]
             struct_data["updata"] = info_dir["attr"]["attr2"]
             struct_data["downdata"] = info_dir["attr"]["attr3"]
             struct_data["finish_updata_flag"] = True
             print(struct_data)