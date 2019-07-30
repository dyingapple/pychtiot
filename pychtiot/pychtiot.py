# -*- coding: utf-8 -*-

import os
import json
import uuid
import time
import random
import thread
import datetime
import paho.mqtt.client as mqtt

server = "iot.cht.com.tw"
client_id = str(uuid.uuid1())
clients = []

class chtiot_mqtt:
  def __init__(self, CK=None, deviceId=None, sensorId=None, jsonFile=None):
    self.CK = CK
    self.did = deviceId
    self.sid = sensorId
    if jsonFile is not None:
        try:
            f = json.loads(open(jsonFile).read())
            print(f)
            self.CK = f["CK"]
            self.did = f["deviceId"]
            self.sid = f["sensorId"]
        except:
            print("jsonfile read failed")
    if self.CK is None:
        print("Please recheck your CK key")
        raise SystemExit(0)
    if self.did is None:
        print("Please recheck your deviceId")
        raise SystemExit(0)
    if self.sid is None:
        print("Please recheck your sensorId")
        raise SystemExit(0)
    self.data = []


  def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


  def submessage(self, client, userdata, msg):
    print("topic:" + msg.topic + " " + "payload:" + str(msg.payload))


  def sub_thread(self, service):
    client = mqtt.Client(client_id=client_id)
    client.username_pw_set(self.CK,self.CK)
    conn = client.connect(server)
    client.loop_start()
    client.on_message = self.submessage
    client.on_subscribe = self.on_subscribe
    if service == "heartbeat":
      client.subscribe(("/v1/device/"+self.did+"/heartbeat", 1))
    else:
      client.subscribe(("/v1/device/"+self.did+"/sensor/"+self.sid+"/" + service , 1))


  def sub(self, service="rawdata"):
    try:
      time.sleep(1)
      thread.start_new_thread(self.sub_thread, (service, ))
    except:
      print("thread error")


  def pub(self, seconds, service="rawdata"):
    try:
      time.sleep(1)
      thread.start_new_thread(self.pub_thread, (seconds, service, ))
    except:
      print("thread error")


  def pub_thread(self, seconds, service):
    client = mqtt.Client(client_id=client_id)
    client.username_pw_set(self.CK,self.CK)
    conn = client.connect(server)
    client.loop_start()
    time.sleep(seconds)
    while True:
      if service == "rawdata":
        value = {}
        value["value"] = self.data
        value["id"] = self.sid
        try:
          value["lat"] = self.lat
        except:
          pass
        try:
          value["lon"] = self.lon
        except:
          pass
        try:
          value["time"] = self.time
        except:
          value["time"] = datetime.datetime.now().isoformat()
        payload = json.dumps([value])
      elif service == "heartbeat":
        payload = json.dumps({"pulse":str(seconds)})
      client.publish("/v1/device/"+self.did+"/"+service , payload=payload)
      time.sleep(seconds)

  def pub_loc(self, lat=None, lon=None):
    if isinstance(lat, float) or isinstance(lat, int):
      self.lat = lat
    else:
      print("lat is not a number")
    if isinstance(lon, float) or isinstance(lon, int):
      self.lon = lon
    else:
      print("lon is not a number")

  def pub_time(self, t=datetime.datetime.now().isoformat()):
    self.time = t

  def pub_data(self, *data):
    dataCount = len(data)
    if dataCount == 0:
      self.data = ""
    else:
      self.data = []
      for i in range(dataCount):
        self.data.append(str(data[i]))


if __name__ == "__main__":
  pass
