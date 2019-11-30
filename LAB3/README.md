# LAB3_OM2M with Postman
## 目標:
    使用Postman分別建立以下Entities
	1. Create a "MY_SENSOR" Application
		2. Create a "DESCRIPTOR" container
			3. Create a "DESCRIPTOR contentInsances"
		4. Create a "DATA" container
			5. Create a "DATA contentInsances"
			6. Create a "Subscription" contact to localhost:1400/monitor

## 作法or步驟:
1. Open GSCL and NSCL services
    - GSCL : localhost:8181
    - NSCL : localhost:8080
![](https://i.imgur.com/LgU14A2.png)

2. Retrieve a resource from GSCL
![](https://i.imgur.com/3D43qRp.png)
![](https://i.imgur.com/hFJfx57.png)
![](https://i.imgur.com/UspQ3Fg.png)

3. Create a "MY_SENSOR" Application in GSCL
![](https://i.imgur.com/aCM3MPn.png)
![](https://i.imgur.com/KyEKWVQ.png)
![](https://i.imgur.com/AA7wcsw.png)
![](https://i.imgur.com/7CSA784.png)

4. Create a "DESCRIPTOR" container in GSCL
![](https://i.imgur.com/rnVS3kk.png)
![](https://i.imgur.com/NmAsLH5.png)
![](https://i.imgur.com/kIDrskI.png)
![](https://i.imgur.com/M2sqVjO.png)

5. Create a "DESCRIPTOR contentInsances" in GSCL
![](https://i.imgur.com/BjHaINo.png)
![](https://i.imgur.com/twGFXBY.png)
![](https://i.imgur.com/LKrQAze.png)
![](https://i.imgur.com/cNcG9vH.png)

6. Create a "DATA" container in GSCL
![](https://i.imgur.com/mOFCwtN.png)
![](https://i.imgur.com/okb2qes.png)
![](https://i.imgur.com/SZ2Pd1P.png)
![](https://i.imgur.com/ah05HEN.png)

7. Create a "DATA contentInsances" in GSCL
![](https://i.imgur.com/aQCBO6c.png)
![](https://i.imgur.com/ylq3QP2.png)
![](https://i.imgur.com/XY3mXIo.png)
![](https://i.imgur.com/yVyWHgg.png)

8. Create a "Subscription" contact to "localhost:1400/monitor"
![](https://i.imgur.com/ZQBnFhJ.png)
![](https://i.imgur.com/HSveuIh.png)
![](https://i.imgur.com/kOb8fpH.png)
![](https://i.imgur.com/eAeGLiS.png)

# LAB3_OM2M GA with Node-red(GA.json)
## 目標:
    使用 node-red 在GSCL分別建立以下 Entities
	1. Create a "MY_SENSOR" Application
		2. Create a "DESCRIPTOR" container
			3. Create a "DESCRIPTOR contentInsances"
		4. Create a "DATA" container
			5. Create a "DATA contentInsances"
	6. 在 GA(node-red) 開啟 /sensorData Server 負責轉傳 data 到 OM2M
	

## 作法or步驟:
1. Open GSCL and NSCL services
    - GSCL : localhost:8181
    - NSCL : localhost:8080
![](https://i.imgur.com/LgU14A2.png)

2. Open Node-red services
    - Node-red : localhost:1880
![](https://i.imgur.com/aYFzJu1.png)

3. Create a "MY_SENSOR" Application
![](https://i.imgur.com/6ZxF2wm.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/SAkgMAs.png)
![](https://i.imgur.com/H8RWFtT.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/7HhrWAV.png)
![](https://i.imgur.com/Gqp9FpO.png)

4. Create a "DESCRIPTOR" container
![](https://i.imgur.com/YS8f06P.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/zlfRokB.png)
![](https://i.imgur.com/H8RWFtT.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/sLwrbqk.png)
![](https://i.imgur.com/N7lW3Ur.png)

5. Create a "DESCRIPTOR contentInsances"
![](https://i.imgur.com/mHtEGQA.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/HWJijRR.png)
![](https://i.imgur.com/H8RWFtT.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/QZg4vlY.png)
![](https://i.imgur.com/nMB7Zgm.png)

6. Create a "DATA" container
![](https://i.imgur.com/F2JOsiS.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/66m977B.png)
![](https://i.imgur.com/H8RWFtT.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/apO9yAg.png)
![](https://i.imgur.com/A5EwKgG.png)

7. Create a "DATA contentInsances"
![](https://i.imgur.com/77Afa9x.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/Z5FGFdL.png)
![](https://i.imgur.com/ulnbGtc.png)
![](https://i.imgur.com/H8RWFtT.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/lbtXbUC.png)
![](https://i.imgur.com/s9tzccN.png)

8. 在 GA(node-red) 開啟 /sensorData Server 負責轉傳 data 到 OM2M
![](https://i.imgur.com/ANLnYSO.png)
![](https://i.imgur.com/oiEUIBq.png)
![](https://i.imgur.com/tZcgiWt.png)
![](https://i.imgur.com/4uxeK96.png)
![](https://i.imgur.com/a6uAQPI.png)
![](https://i.imgur.com/hEGFEga.png)
![](https://i.imgur.com/bLRp8kN.png)
![](https://i.imgur.com/DfVqpWj.png)
![](https://i.imgur.com/BBcNcVR.png)
![](https://i.imgur.com/QO175Do.png)
![](https://i.imgur.com/zk0bA4M.png)


# LAB3_OM2M NA with Node-red(NA.json)
## 目標:
    使用 node-red 在 NSCL 分別建立以下 Entities
	1. Create a "MY_NETWORK_APPLICATION"
	2. Subscribe new contentInsatnace in the   gscl/MYSENSOR/DATA 並儲存
	3. 開啟 /getxmlfile Server 負責讀取先前儲存的資料
    
## 作法or步驟:
1. Finish LAB3_OM2M GA with Node-red.
    - 完成前面GA配置

2. Create a "MY_NETWORK_APPLICATION"
![](https://i.imgur.com/sBWofHq.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/z8yok9K.png)
![](https://i.imgur.com/H8RWFtT.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/1BMGOIb.png)
![](https://i.imgur.com/F7RHanJ.png)

3. Subscribe new contentInsatnace in the gscl/MY_SENSOR/DATA 並儲存
![](https://i.imgur.com/wN52xOV.png)
![](https://i.imgur.com/LnxXWVW.png)
![](https://i.imgur.com/2q8z6Ql.png)
![](https://i.imgur.com/XvCoFfJ.png)
![](https://i.imgur.com/K9EQX6k.png)
![](https://i.imgur.com/1I8VPtx.png)
![](https://i.imgur.com/H7T2h4b.png)

4. 開啟 /getXMLfile Server 負責讀取先前儲存的資料
![](https://i.imgur.com/OB7sswo.png)
