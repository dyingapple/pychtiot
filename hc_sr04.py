#!/usr/bin/python
# -*- coding: utf-8 -*-.

import time
import random
import RPi.GPIO as GPIO
from pychtiot import chtiot_mqtt

'''
CK可以從https://iot.cht.com.tw/iot/quickstart中，點擊該專案的編輯專案按鈕->權限資料->專案金鑰中取得
deviceId 可在專案內，選擇編輯設備按鈕中取得
sensorId 可在設備中，編輯感測器中取得
'''
CK = "PK2TTKBUGE3AYX34A9"
deviceId = "16617392521"
sensorId = "nbiot"

def main():
  ## GPIO設定成BCM腳位
  GPIO.setmode(GPIO.BCM)
  GPIO_TRIGGER = 23
  GPIO_ECHO = 24
  GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
  GPIO.setup(GPIO_ECHO, GPIO.IN)
  GPIO.output(GPIO_TRIGGER, False)

  ## 若僅有單一感測器可直接使用CK, deviceId, sensorId等等變數，也可以以字串的形式直接寫入(多感應器情況下建議後者)
  sensor1 = chtiot_mqtt("PK2TTKBUGE3AYX34A9", "16617392521", "nbiot")
  #sensor1 = chtiot_mqtt(CK, deviceId, sensorId)

  ## 使用專案精靈
  ## 請將上方sensor1 .....最前方加入#，並將下方ck.json改成同資料夾內剛下載的json名稱
  #sensor1 = chtiot_mqtt(jsonFile="ck.json")

  ## 下方為mqtt的subscribe功能，當伺服器有新的資料，訂閱可以隨時被通知並輸出到終端機上
  #sensor_name.sub()         
  sensor1.sub()
  
  ## pub是mqtt中的publish，在IoT大平台中，可利用mqtt做幾項功能的推送，其中下方的service(不填寫)預設為rawdata
  ## 時間請至少>=1秒
  ##   .pub( seconds, [service=rawdata] )
  ##      seconds: time period between two data sent
  ##      service: rawdata, heartbeat, cmd, ack

  sensor1.pub(30)

  ## 下方以隨機生成兩個數字當作資料，並寫入pub_data函式中以供為下次更新提交給伺服器的資料
  ## 範例中迴圈以10秒一次擷取一次超音波感測器資料，並在每次間隔30秒的時候跟伺服器更新資料
  ## 時間請至少>=1秒
  # pub_data(self, *data)
  # pub_loc(lat=None, lon=None)

  try:
    while True:
      GPIO.output(GPIO_TRIGGER, True)
      time.sleep(0.00001)
      GPIO.output(GPIO_TRIGGER, False)
      start = time.time()
      while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
      while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()


      t = stop - start
      d = t * 34300 / 2
      print("D = %.1f" % d)
      sensor1.pub_data(d)
      time.sleep(10)
  except:
    print("exit...")
    GPIO.cleanup()

if __name__ == '__main__':
  main()
