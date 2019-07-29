#!/usr/bin/python
# -*- coding: utf-8 -*-.

import time
import random
from pychtiot import chtiot_mqtt


'''
CK可以從https://iot.cht.com.tw/iot/quickstart中，點擊該專案的編輯專案按鈕->權限資料->專案金鑰中取得

deviceId
sensorId
'''

CK = "PK2TTKBUGE3AYX34A9"
deviceId = "16617392521"
sensorId = "nbiot"

def main():
  # 若僅有單一感測器可直接使用CK, deviceId, sensorId等等變數，也可以以字串的形式直接寫入
  #sensor_name = chtiot_mqtt( CK, deviceId, sensorId )
  nbiot = chtiot_mqtt("PK2TTKBUGE3AYX34A9", "16617392521", "nbiot")

  # 下方為mqtt的subscribe功能，當伺服器有新的資料，訂閱可以隨時被通知並輸出到終端機上
  #sensor_name.sub()         
  nbiot.sub()
  
  # pub是mqtt中的publish，在IoT大平台中，可利用mqtt做幾項功能的推送，其中下方的service(不填寫)預設為rawdata
  #   .pub( seconds, [service=rawdata] )
  #      seconds: time period between two data sent
  #      service: rawdata, heartbeat, cmd, ack

  nbiot.pub(30)

  # 下方以隨機生成兩個數字當作資料，並寫入pub_data函式中以供為下次更新提交給伺服器的資料
  # 範例中迴圈以8秒一次讀取RPi感測器資料，並在每次間隔60秒的時候跟伺服器更新資料
  ## pub_data(self, *data)
  ## pub_loc(lat=None, lon=None)
  while True:
    random1 = random.randrange(1000, 4000) / 100.00
    random2 = random.randrange(1000, 4000) / 100.00
    random3 = "atatat"
    random4 = {"qq":"bb"}
    nbiot.pub_data(random1,random2,random3, random4)
    time.sleep(5)


if __name__ == '__main__':
  main()
