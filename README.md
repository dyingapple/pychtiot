# CHT IoT 大平台 RaspberryPi快速連接包/新手包


## 環境
- RaspberryPi 3B v1.2
  - Raspbian version 10 (buster)
  - Python 2.7.16
    - paho-mqtt 1.14.0
- HC-SR04
- DHT22 (@尚未補完)

## 範例程式
- basic.py 僅有簡單的資料發送接收功能，提供使用者做基本的連線測試
- hc_sr04.py 超音波感測器範例
- (@尚未補完)

## 開啟專案
1. 請先連上大平台並登入(https://iot.cht.com.tw/iot/quickstart)

2. 第一次使用可點擊專案精靈按鈕(請跳步驟3a)，若需細部編輯可選擇增加專案(請跳步驟3b)

3. a) 新增完成後，請下載連結中的JSON檔案，複製進與Code同個檔案夾中
   b) 設定完專案後需要新增設備，以及在該設備底下新增感應器，並從編輯專案、編輯設備、編輯感測器中分別取得三個金鑰（專案、設備、感測器），此三組金鑰會在下面步驟使用到


## 程式執行步驟
1. 文字介面使用者請輸入`git clone https://github.com/dyingapple/pychtiot.git`，圖形介面使用者請至網頁https://github.com/dyingapple/pychtiot/archive/master.zip下載後解壓縮

2. 請使用終端機進入此資料夾內輸入`pip -r requirements.txt`安裝相關套件

3. 修改basic.py或(@尚未補完)，並選擇更改金鑰方式
   a) 下載JSON檔案，並請按照Code內註解指示變更內容
   b) 將取得的金鑰分別填入CK, deviceId, sensorId中，並註解....mqtt(jsonFile=...)那行

4. 基本測試：執行`python basic.py` 或在圖形介面中點擊`basic.py`兩下
   若已接上特定感應器做測試：在文字介面執行`python xxxx.py` 或在圖形介面中滑鼠點擊xxxx兩下

5. 更進一步：修改basic.py或hc_sr04.py或pychtiot/pychtiot.py檔案做更進一步的功能(增加GPIO等等)

## 平台相關資料
- 大平台MQTT subscribe/publish https://iot.cht.com.tw/iot/developer/mqtt
- 大平台其他進階範例程式 https://iot.cht.com.tw/iot/developer/download
- RPi + DHT22 + pm2.5 詳細作法 https://iot.cht.com.tw/iot/developer/resources/iot/download/DeviceConnMgt/Raspberry_Connect_IoT_Example.pdf
