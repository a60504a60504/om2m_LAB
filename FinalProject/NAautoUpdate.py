import time
import ast
import requests
from timeloop import Timeloop
from datetime import timedelta
import xml.etree.ElementTree as ET

BasicAuth = requests.auth.HTTPBasicAuth('admin', 'admin')
GSCLURIhead = "http://localhost:8181/om2m/gscl"
GAURI = "http://localhost:5000"
LevelName = ["Off","Week","Mid","Strong","Error"]

tl = Timeloop()


@tl.job(interval=timedelta(seconds=5))
def FanControlPolling():
    with open("Control.txt") as txt:
        [A,B,C] = ast.literal_eval(txt.read())
    
    Temp = 0
    r = requests.get(GSCLURIhead+"/applications/Thermometer/containers/DATA/contentInstances/latest/content", auth=BasicAuth)
    root = ET.fromstring(r.content)
    for data in root.iter('int'):
        if (data.attrib['name']=='data'):
            Temp = int(data.attrib['val'])
    originFan = 0
    r = requests.get(GSCLURIhead+"/applications/Fan/containers/DATA/contentInstances/latest/content", auth=BasicAuth)
    root = ET.fromstring(r.content)
    for data in root.iter('int'):
        if (data.attrib['name']=='data'):
            originFan = int(data.attrib['val'])
    
    if Temp > A:
        Fan = 3
    elif Temp > B:
        Fan = 2
    elif Temp > C:
        Fan = 1
    else:
        Fan = 0
    if originFan != Fan:
        payload = {'data':str(Fan)}
        r = requests.post(GAURI+'/UpdateFan', json=payload)
    print([originFan,Fan,Temp,A,B,C])



if __name__ == "__main__":
    tl.start(block=True)