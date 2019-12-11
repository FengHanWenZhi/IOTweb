
host_ip = "192.168.43.51"
host_port = 1883
qos = 0

c_to_s_kv = {}    #用来存放客户端到服务器的消息，主键时消息id;
s_to_c_kv = {"runner/ucas/ucas/sub/actor/set":"runner/ucas/ucas/sub/actor/set come in 1","runner/ucas/ucas/sub/actor/get":"runner/ucas/ucas/sub/actor/get come in 2","runner/ucas/ucas/sub/sensor/get":"runner/ucas/ucas/sub/sensor/get come in 3"}   #用来存放服务器到客户端的消息，主键时s_to_c 的topic;
ser_need_sub_topic_list = ["HumiditySensor/ucas/ucas/pub/actor/status","FloodlightSensor/ucas/ucas/pub/actor/status","TemperatureSensor/ucas/ucas/pub/actor/status","TemperatureSensor/ucas/ucas/pub/sensor/status"]   #服务器端待订阅的主题；由客户端上报信息；
ser_have_sub_topic_list = []    #服务器端已经订阅的主题；
ser_need_unsub_topic_list = []   #服务器端需要取消订阅的主题；

