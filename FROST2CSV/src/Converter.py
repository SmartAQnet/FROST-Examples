#!/usr/bin/env python
# coding: utf-8

# # imports

# In[ ]:


import os
import json
import dateutil
import datetime
import csv
import SensorThings as st


# # export notebook

# In[ ]:


if __name__ == "__main__":
    try:
        get_ipython()
        isnotebook = True
    except Exception:
        isnotebook = False
    
    if isnotebook:
        get_ipython().system('jupyter nbconvert --to script Converter.ipynb')


# # settings

# In[ ]:


reloaddata = True

ThingID = "testthing"
starttime = "2018-11-15T00:00:00.000Z"
endtime = "2018-11-16T23:59:59.999Z"

st_url = "http://smartaqnet.teco.edu:8080/FROST-Server"


# # get all DatastreamIDs

# In[ ]:


where = "/v1.0/Things('" + ThingID + "')/Datastreams"
qdata = ["$select=id"]

DatastreamIDs = st.GetEntities(st_url, where, qdata)
DatastreamIDs = [
    elem["@iot.id"] for elem in DatastreamIDs
]


# # get all Observations

# In[ ]:


qdata = [
    "$expand=" +
        "Datastream($select=id)," + 
        "FeatureOfInterest($select=id,feature)",
    
    "$filter=" +
        "phenomenonTime ge " + starttime + " and "
        "phenomenonTime le " + endtime,
    
    "$select=id,result,phenomenonTime"
]

data = list()
csvheader = [
    "DatastreamID",
    "ObservationID",
    "FeatureOfInterestID",
    "date",
    "value",
    "timestamp",
    "longitude",
    "latitude",
    "elevation"
]

basepath = "./" + ThingID.replace(":", "-")
if not os.path.exists(basepath):
    os.makedirs(basepath)

for did in DatastreamIDs:
    filename = basepath + "/Observations_" + did.replace(":", "-") + ".json"
    if (not os.path.isfile(filename)) or reloaddata:
        where2 = where + "('" + did + "')/Observations"
        Observations = st.GetEntities(st_url, where2, qdata)
        with open(filename, "w") as file:
            json.dump(Observations, file)
    else:
        with open(filename, "r") as file:
            Observations = json.load(file)
            
    tempdata = [
        [
            obs["Datastream"]["@iot.id"],
            obs["@iot.id"],
            obs["FeatureOfInterest"]["@iot.id"],
            obs["phenomenonTime"],
            obs["result"],
            dateutil.parser.parse(obs["phenomenonTime"]).timestamp(),
            *(obs["FeatureOfInterest"]["feature"]["coordinates"])
        ]
        for obs in Observations
    ]
    tempdata.sort(key=lambda x: x[5])
    
    filename = basepath + "/Observations_" + did.replace(":", "-") + ".csv"
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(csvheader)
        for elem in tempdata:
            csvwriter.writerow(elem)
    
    data.extend(tempdata)
    
with open(basepath + "/alldata.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(csvheader)
    for elem in data:
        csvwriter.writerow(elem)


# In[ ]:




