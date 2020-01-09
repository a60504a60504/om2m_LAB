import requests
import xml.etree.ElementTree as ET
from http import HTTPStatus
from flask import Flask, request


app = Flask(__name__)
BasicAuth = requests.auth.HTTPBasicAuth('admin', 'admin')
GSCLURIhead = "http://localhost:8181/om2m/gscl"
GAURI = "http://localhost:5000"
LevelName = ["Off","Week","Mid","Strong","Error"]



@app.route("/GetTemp", methods=['GET'])
def GetTemp():
    ans = -1
    r = requests.get(GSCLURIhead+"/applications/Thermometer/containers/DATA/contentInstances/latest/content", auth=BasicAuth)
    root = ET.fromstring(r.content)
    for data in root.iter('int'):
        if (data.attrib['name']=='data'):
            ans = data.attrib['val']
    return ans



@app.route("/GetFan", methods=['GET'])
def GetFan():
    ans = -1
    r = requests.get(GSCLURIhead+"/applications/Fan/containers/DATA/contentInstances/latest/content", auth=BasicAuth)
    root = ET.fromstring(r.content)
    for data in root.iter('int'):
        if (data.attrib['name']=='data'):
            ans = int(data.attrib['val'])
    return LevelName[ans]



@app.route("/SetFan", methods=['POST'])
def SetFan():
    global A,B,C
    A = int(request.json['A'])
    B = int(request.json['B'])
    C = int(request.json['C'])
    with open("Control.txt",'w') as txt:
        txt.write(str([A,B,C]))
    return "200"



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5001,use_reloader=False)
