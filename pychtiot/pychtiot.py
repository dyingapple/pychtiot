# -*- coding: utf-8 -*-

import os
import json
import uuid
import time
import random
import thread
import paho.mqtt.client as mqtt

server = "iot.cht.com.tw"
client_id = str(uuid.uuid1())


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

    self.client = mqtt.Client(client_id=client_id)
    self.client.username_pw_set(self.CK,self.CK)
    self.conn = self.client.connect(server)
    self.client.loop_start()
    self.data = []

  def submessage(self, client, userdata, msg):
    print("topic:" + msg.topic + " " + "payload:" + str(msg.payload))

  def sub(self, service="rawdata"):
    self.client.subscribe("/v1/device/"+self.did+"/sensor/"+self.sid+"/" + service , 1)
    self.client.on_message = self.submessage

  def pub(self, seconds, service="rawdata"):
    try:
      time.sleep(1)
      thread.start_new_thread(self.pub_thread, (seconds, service, ))
    except:
      print("thread error")

  def pub_thread(self, period, service):
    time.sleep(period)
    while True:
      value = {}
      value["value"] = self.data
      value["id"] = self.sid
      time.sleep(1)
      payload = json.dumps([value])
      i = self.client.publish("/v1/device/"+self.did+"/"+service , payload=payload)
      time.sleep(period-1)

  def pub_loc(self, lat=None, lon=None):
    self.lat = lat
    self.lon = lon

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
