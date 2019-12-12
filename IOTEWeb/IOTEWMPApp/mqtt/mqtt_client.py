import paho.mqtt.client as mqtt
import mqtt_data
import struct_data as m_sdi
import _thread
import time


# 为线程定义一个函数
def struct_data_thread( threadName, delay):
   while 1:
      time.sleep(delay)
      if(mqtt_data.c_to_s_kv):
           print("if(mqtt_data.c_to_s_kv):")
           m_sdi.rawinfo_to_structdata(mqtt_data.c_to_s_kv, m_sdi.struct_data)
      # else:
      #      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))









def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #print("shoudao : %s",str(msg.payload))
    payload = str(msg.payload)
    info = payload[2:-1]
    item = {str(msg.topic):info}
    print("save:  : ",end = " ");
    print(item);
    mqtt_data.c_to_s_kv.update(item);

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
#    print("Subscribed: " + str(mid) + " " + str(granted_qos) + "\n\r")
     mid = mid + 1;


def on_log(mqttc, obj, level, string):
    print(string)



def mqtt_server_thread( threadName, delay):

    #print("%s: %s   start " % (threadName, time.ctime(time.time())));

    # Uncomment to enable debug messages
    # mqttc.on_log = on_log

    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.connect(mqtt_data.host_ip, mqtt_data.host_port, 60)
    #mqttc.subscribe("$SYS/#", 0)

    mqttc.loop_start();

    while 1:
        time.sleep(delay)
        #print("%s: %s runing " % (threadName, time.ctime(time.time())))
        #SUB TOPIC
        while mqtt_data.ser_need_sub_topic_list:
            s = mqtt_data.ser_need_sub_topic_list.pop(0);
            mqttc.subscribe(s, mqtt_data.qos);
            mqtt_data.ser_have_sub_topic_list.append(s);
        # print(mqtt_data.ser_have_sub_topic_list)
        #PUB MESSAGE
        while mqtt_data.s_to_c_kv:
            reversed_kv = {};  #反转键值对在字典中的顺序，前面的键值对放到后面，一会儿会从后面开始弹出；
            while mqtt_data.s_to_c_kv:
                k,v = mqtt_data.s_to_c_kv.popitem();
                item = {k:v};
                reversed_kv.update(item);
            while reversed_kv:
                s_topic,s_payload = reversed_kv.popitem();
                #print(s_topic,s_payload);
                print("pub:",end = " ")
                print(s_topic)
                infot = mqttc.publish(s_topic, s_payload, mqtt_data.qos)
                infot.wait_for_publish()

try:
   _thread.start_new_thread( struct_data_thread, ("struct_data_thread", 0.1, ) )
   _thread.start_new_thread(mqtt_server_thread, ("mqtt_server_thread", 0.1) )
except:
   print ("Error: struct_data_thread 无法启动线程")

# while 1:
#     time.sleep(10)
# def matt_thread( threadName, delay):
#     while 1:
#         time.sleep(delay)
#         #SUB TOPIC
#         while mqtt_data.ser_need_sub_topic_list:
#             s = mqtt_data.ser_need_sub_topic_list.pop(0);
#             mqttc.subscribe(s, mqtt_data.qos);
#             mqtt_data.ser_have_sub_topic_list.append(s);
#
#         #PUB MESSAGE
#         while mqtt_data.s_to_c_kv:
#             reversed_kv = {};  #反转键值对在字典中的顺序，前面的键值对放到后面，一会儿会从后面开始弹出；
#             while mqtt_data.s_to_c_kv:
#                 k,v = mqtt_data.s_to_c_kv.popitem();
#                 item = {k:v};
#                 reversed_kv.update(item);
#             while reversed_kv:
#                 s_topic,s_payload = reversed_kv.popitem();
#                 #print(s_topic,s_payload);
#                 print("pub:",end = " ")
#                 print(s_topic)
#                 infot = mqttc.publish(s_topic, s_payload, mqtt_data.qos)
#                 infot.wait_for_publish()

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.

#
# # def matt_thread( threadName, delay):
# mqttc = mqtt.Client()
# mqttc.on_message = on_message
# mqttc.on_connect = on_connect
# mqttc.on_publish = on_publish
# mqttc.on_subscribe = on_subscribe
# # Uncomment to enable debug messages
# # mqttc.on_log = on_log
#
#
# mqttc.connect(mqtt_data.host_ip, mqtt_data.host_port, 60)
# #mqttc.subscribe("$SYS/#", 0)
#
# mqttc.loop_start();
#
#
#
# while 1:
#     time.sleep(delay)
#     #SUB TOPIC
#     while mqtt_data.ser_need_sub_topic_list:
#         s = mqtt_data.ser_need_sub_topic_list.pop(0);
#         mqttc.subscribe(s, mqtt_data.qos);
#         mqtt_data.ser_have_sub_topic_list.append(s);
#
#     #PUB MESSAGE
#     while mqtt_data.s_to_c_kv:
#         reversed_kv = {};  #反转键值对在字典中的顺序，前面的键值对放到后面，一会儿会从后面开始弹出；
#         while mqtt_data.s_to_c_kv:
#             k,v = mqtt_data.s_to_c_kv.popitem();
#             item = {k:v};
#             reversed_kv.update(item);
#         while reversed_kv:
#             s_topic,s_payload = reversed_kv.popitem();
#             #print(s_topic,s_payload);
#             print("pub:",end = " ")
#             print(s_topic)
#             infot = mqttc.publish(s_topic, s_payload, mqtt_data.qos)
#             infot.wait_for_publish()





