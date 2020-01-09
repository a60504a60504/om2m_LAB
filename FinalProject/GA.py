import requests
import xml.etree.ElementTree as ET
from http import HTTPStatus
from flask import Flask, request

BasicAuth = requests.auth.HTTPBasicAuth('admin', 'admin')
GSCLURIhead = "http://localhost:8181/om2m/gscl"

app = Flask(__name__)



@app.route("/GetGSCL")
def GetGSCL():
    r = requests.get(GSCLURIhead, auth=BasicAuth)
    return r.content



@app.route("/CreateApp")
def CreateApp():
    with open("ApplicationThermometer.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    with open("ApplicationFan.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    return "200"



@app.route("/CreateDescriptor")
def CreateDescriptor():
    with open("Descriptor.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications/Thermometer/containers", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
        r = requests.post(GSCLURIhead+"/applications/Fan/containers", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    with open("DescriptorThermometer.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications/Thermometer/containers/DESCRIPTOR/contentInstances", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    with open("DescriptorFan.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications/Fan/containers/DESCRIPTOR/contentInstances", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    return "200"
    
    
    
@app.route("/CreateData")
def CreateData():
    with open("Data.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications/Thermometer/containers", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
        r = requests.post(GSCLURIhead+"/applications/Fan/containers", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    return "200"



@app.route("/UpdateTemperature", methods=['POST'])
def UpdateTemperature():
    print(request.json)
    Temp = request.json['data']
    tree = ET.parse("DataThermometer.xml")
    root = tree.getroot()
    for child in root:
        if (child.attrib['name']=='data'):
            child.attrib['val'] = str(Temp)
    tree.write("DataThermometer.xml")
    with open("DataThermometer.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications/Thermometer/containers/DATA/contentInstances", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    return "200"
        
        
        
@app.route("/UpdateFan", methods=['POST'])
def UpdateFan():
    Intensity = request.json['data']
    tree = ET.parse("DataFan.xml")
    root = tree.getroot()
    for child in root:
        if (child.attrib['name']=='data'):
            child.attrib['val'] = str(Intensity)
    tree.write("DataFan.xml")
    with open("DataFan.xml") as xml:
        payload = xml.read()
        r = requests.post(GSCLURIhead+"/applications/Fan/containers/DATA/contentInstances", auth=BasicAuth, data=payload)
        app.logger.info(str(HTTPStatus(r.status_code)))
    return "200"



@app.route("/GetFan", methods=['GET'])
def GetFan():
    ans = -1
    r = requests.get(GSCLURIhead+"/applications/Fan/containers/DATA/contentInstances/latest/content", auth=BasicAuth)
    root = ET.fromstring(r.content)
    for data in root.iter('int'):
        if (data.attrib['name']=='data'):
            ans = data.attrib['val']
    return ans



if __name__ == "__main__":
    CreateApp()
    CreateDescriptor()
    CreateData()
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
