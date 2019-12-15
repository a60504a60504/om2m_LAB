# 檔案說明:
- LampControl.aia
    - LAB5 App Inventor專案檔
- LampControl.apk
    - LAB5 App 安裝檔
- flows.json
    - LAB5 Node-red設定檔

# LAB5
## 目標:
    使用任意方法完成以下:
    1. 分別控制 LAMP_0 的開/關、LAMP_1 的開/關、ALL_ON、ALL_OFF 共六個動作
    2. 在 APP 上，顯示當前燈泡的狀態 (主動 or 被動皆可)

## 作法or步驟:  
1. 完成手機App設計
    - ![](https://i.imgur.com/lasAOYX.png)
    - ![](https://i.imgur.com/opaWj22.png)
    - Web1
        - URL:http://192.168.0.3:1880/LAB5
    - Web2
        - URL:http://192.168.0.3:1880/LAB5_LampStatus
    - Clock1
        - Time Interval: 1000ms

2. 完成Node-red GA轉送設計
    - ![](https://i.imgur.com/2WroTzS.png)
    - 產生4條flow:
        - [POST]/LAB5: 發送命令到GSCL
        - Subscribe to Lamp0/1: 在GSCL建立subscription到http://localhost:1880/LAB5_sub
        - [POST]/LAB5_sub: 將獲得的燈泡狀態儲存分別儲存至0.xml與1.xml
        - [GET]/LAB5_LampStatus: 將儲存的燈泡狀態資訊包裝成list格式輸出(e.g. [true,false])
3. 測試成果
    - 開啟GSCL與NSCL
    - 在GSCL輸入ss後按下ENTER鍵
    - 確認org.eclipse.om2m ipu.sample為第25位
    - 輸入start 25後按下ENTER鍵
    - 出現虛擬燈泡程式
        ![](https://i.imgur.com/RoLIapv.png)
    - 安裝並開啟手機APP:LampControl
        ![](https://i.imgur.com/iWXqMgX.png)
    - APP隨時(每1s)向GA詢問燈泡最新狀態並轉送控制信息
