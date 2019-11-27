# LAB2_Get_Sensor_Value(GetSensorValue.aia)
## 目標:
    按下按鈕時，抓取手機上的三種sensor，Accelerometer、OrientationSensor、LocationSensor
    
## 作法or步驟: 
1. 完成Flow Design
![](https://i.imgur.com/8Dh6hbi.png)

2. 完成Block Design
![](https://i.imgur.com/8mOh6r4.png)

3. 以AIA檔案儲存並產生APK檔案輸出
![](https://i.imgur.com/t8X1kzm.png)
![](https://i.imgur.com/eHvRItO.png)

4. 運行結果
![](https://i.imgur.com/SBZ4IIK.png)


# LAB2_Show_Location_on_Google.aia(ShowLocationOnGoogle.aia)
## 目標:
    實現五個功能，1.抓取LocationSensor(GPS) 2.將1中的值傳到node-red顯示 3.讀取server存放的location資料 4(5).將1(3)中的資料用google map定位 

## 作法or步驟:
1. 完成Flow Design
![](https://i.imgur.com/olmGhmb.png)

2. 完成Block Design 注意ServerIP為192.168.0.3:1880
![](https://i.imgur.com/euk6Og9.png)

3. 以AIA檔案儲存並產生APK檔案輸出
![](https://i.imgur.com/t8X1kzm.png)
![](https://i.imgur.com/eHvRItO.png)

4. 運行結果
![](https://i.imgur.com/PlLxJCr.png)

# LAB2_flow.json(flows.json)
## 目標:
    1.接受來自app的訊息，並回復response，2.回傳在server儲存的location data
    
## 作法or步驟:
1. 完成Flow Design
![](https://i.imgur.com/x9ApdZr.png)
![](https://i.imgur.com/Uw2cDor.png)
![](https://i.imgur.com/p4yn1Ak.png)
![](https://i.imgur.com/hk3WLxG.png)


2. Deploy

3. 下載並儲存成JSON格式
![](https://i.imgur.com/lIDv7xq.png)