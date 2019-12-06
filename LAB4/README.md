# 檔案說明:
- GA.json
    - LAB4_GA with Node-red各節點設定檔
- LAB4LocationSenderGA.aia
    - LAB4_App inventor Sender的AppInventor專案檔
- LAB4LocationSenderGA.apk
    - LAB4_App inventor Sender的手機安裝檔
- NA.json
    - LAB4_NA with Node-red各節點設定檔
- LAB4LocationShowOnNA.aia
    - LAB4_APP Inventor reciver的AppInventor專案檔
- LAB4LocationShowOnNA.apk
    - LAB4_APP Inventor reciver的手機安裝檔

# LAB4_GA with Node-red
## 目標:
    使用 node-red 分別建立以下
	  1. Create a "Location_Gateway_Application" Application on OM2M
		2. Create a "DESCRIPTOR" container on OM2M
		    3. Create a "DESCRIPTOR contentInsances" on OM2M
		4. Create a "DATA" container on OM2M
			5. Create a "DATA contentInsances" (for testing) on OM2M
    6. Create a http node to forward data to GSCL

## 作法or步驟: 
1. 開啟Node-red(http://localhost:1880/)
2. 開啟GSCL與NSCL
    - GSCL: localhost:8181
    - NSCL: localhost:8080
3. 繪製出以下架構
![](https://i.imgur.com/qfUVYHv.png)
3. 設定各個節點
    - Application
        - xSCL: localhost:8181
        - xA: LOCATION_GATEWAY_APPLICATION
            - ContactURL: localhost:1880
        - Type: Gateway Application
        - Category: Demo
        - Location: NCKU
        - Announce: checked
    - Descriptor-Container/ Descriptor-ContentInstance/ Data-Container/ Data-ContentInstance
        - xSCL: localhost:8181
            - xSCL ID: gscl
            - Host: localhost
            - Port: 8181
            - Base URL: /om2m/
        - xA: LOCATION_GATEWAY_APPLICATION
            - ContactURL: localhost:1880
    - http request
        - use authentication
            - username: admin
            - password: admin
    - function MyData
        ``` java
        var data = {
            type:'gps',
            unit:'float',
            latitude: '1',
            longitude: '2'
        };
        msg.payload = JSON.stringify(data);
        return msg;
        ```
    - function InputData
        ```java
        var data = {
            type:'gps',
            unit:'float',
            latitude: msg.payload.latitude,
            longitude: msg.payload.longitude
        };
        msg.payload = JSON.stringify(data);
        return msg;
        ```
    - HTTP PostSensorData
        - Method: POST
        - URL: /locationData
4. 部屬
![](https://i.imgur.com/zP6H5KE.png)

    
# LAB4_App inventor Sender
## 目標:
    須完成兩個功能
      1.讀取手機(or 模擬器)的location sensor
      2.將其值交給 GA(node-red)
 
## 作法or步驟: 
1. 完成App Inventor的Designers外觀設計
![](https://i.imgur.com/MQGvVv1.png)

2. 完成App Inventor的Blocks邏輯設計
    - Node-red server IP: 192.168.0.3:1880
![](https://i.imgur.com/DxmgC3z.png)

3. 產生APK後執行
![](https://i.imgur.com/IMjlqTJ.png)

4. 開啟GSCL與NSCL與前面部屬的Node-red
5. 測試功能
![](https://i.imgur.com/D36QMdj.png)
![](https://i.imgur.com/JUueyio.png)
![](https://i.imgur.com/01MYqlA.png)

       
# LAB4_NA with Node-red
# 目標:
    使用 node-red 建立以下
    1. Create a "Location_Network_Application" Application on OM2M
    2. Subscribe new contentInsatnace in the   gscl/Location_Gateway_Application/DATA  on OM2M and save recive notify
    3. Create a http node to response previously save data
    
## 作法or步驟: 
1. 開啟Node-red(http://localhost:1880/)
2. 開啟GSCL與NSCL
    - GSCL: localhost:8181
    - NSCL: localhost:8080
3. 繪製出以下架構
![](https://i.imgur.com/rrVqpjN.png)


4. 設定各個節點
    - Application
        - xSCL: localhost:8080
            - xSCL ID: nscl
            - Host: localhost
            - Port: 8080
            - Base URL: /om2m/
        - xA: Location_Network_Application
            - contactURL: localhost:1880
        - Type: Network Application
        - Category: demo 
        - Location: Internet Cloud
    - http request(after Application node)
        - use authentication
            - username: admin
            - password: admin
    - Subscription
        - xSCL: localhost:8080
            - xSCL ID: nscl
            - Host: localhost
            - Port: 8080
            - Base URL: /om2m/
        - xA: Location_Network_Application
            - contactURL: localhost:1880
        - Contact Path: /Location_notification
        - Filter Type: Modified Since
        - Filter Criteria: content
    - http request(after Subscription node)
        - Method: POST
        - URL: http://localhost:8181/om2m/gscl/applications/LOCATION_GATEWAY_APPLICATION/containers/DATA/contentInstances/subscriptions
        - use authentication
            - username: admin
            - password: admin
    - Listen to HTTP POST notification
        - Method: POST
        - URL: /Location_notification
    - Extract Data from XML
        ```java
        var notification = msg.payload['om2m:notify']; 
        var representation = notification['om2m:representation']; 
        var text = representation[0]._; 
        var dataObj = new Buffer(text, 'base64').toString('ascii'); 
        msg.payload = dataObj; 
        return msg;
        ```
    - Extract Location Value
        ```java
        var latitudeName = msg.payload.obj.str[3].$.name;
        var latitudeVal = msg.payload.obj.str[3].$.val;
        var longitudeName = msg.payload.obj.str[4].$.name;
        var longitudeVal = msg.payload.obj.str[4].$.val;

        msg.payload = {
            latitudeName : latitudeVal,
            longitudeName : longitudeVal
        }
        return msg;
        ```
5. 部屬
![](https://i.imgur.com/8zWUh4Q.png)
![](https://i.imgur.com/gt5oZPD.png)

    
# LAB4_APP Inventor reciver
## 目標:
    須完成兩個功能
      1. http get NA(node-red) 上儲存的 data
      2. 將該 data 用來啟動 google map 並顯示位子
      
## 作法or步驟: 
1. 完成App Inventor的Designers外觀設計
![](https://i.imgur.com/hZYyqu8.png)

2. 完成App Inventor的Blocks邏輯設計
    - Node-red server IP: 192.168.0.3:1880
![](https://i.imgur.com/PutCGEm.png)

3. 產生APK後執行
![](https://i.imgur.com/qAyBzTT.png)

4. 開啟GSCL與NSCL與前面部屬的Node-red
5. 測試功能
![](https://i.imgur.com/x2kFuvk.png)
![](https://i.imgur.com/c6BgIz8.png)

