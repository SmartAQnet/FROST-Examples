#!/usr/bin/env python
# coding: utf-8

# # imports

# In[1]:


import requests
import json


# # export notebook

# In[2]:


if __name__ == "__main__":
    try:
        get_ipython()
        isnotebook = True
    except Exception:
        isnotebook = False
        
    if isnotebook:
        get_ipython().system('jupyter nbconvert --to script SensorThings.ipynb')


# # GETRequest

# In[3]:


def GETRequest(url, qdata=None):
    """TODO: add docstring"""
    
    if qdata == None:
        qdata = []
    
    sqdata = "?"
    for elem in qdata:
        sqdata += elem + "&"
    sqdata = sqdata[:-1]

    p = requests.get(url + sqdata)
    body = b""
    for chunk in p.iter_content(chunk_size=128):
        body += chunk
    body = body.decode("utf8")
    body = body.replace("\n", " ").replace("\r", "")
    if (p.status_code  == 200):
        return body
    else:
        raise TypeError(
            "invalid request - status code: " +
            str(p.status_code) +
            " - response: " +
            body
        )


# # GetEntities

# In[4]:


def GetEntities(st_url, where, qdata=None):
    entities = list()

    retval = json.loads(GETRequest(st_url + where, qdata))
    entities.extend(retval["value"])

    allkeys = [*retval]
    while "@iot.nextLink" in allkeys:
        nexturl = retval["@iot.nextLink"]
        retval = json.loads(GETRequest(nexturl))
        entities.extend(retval["value"])
        allkeys = [*retval]

    return entities


# # PATCHRequest

# In[5]:


def PATCHRequest(url, data):
    """TODO: add docstring"""

    p = requests.patch(url, data)
    body = b""
    for chunk in p.iter_content(chunk_size=128):
        body += chunk
    body = body.decode("utf8")
    body = body.replace("\n", " ").replace("\r", "")
    if (p.status_code  == 200):
        return body
    else:
        raise TypeError("invalid request: status code: " + str(p.status_code))


# # Update FeatureOfInterest Coordinates

# In[6]:


def UpdateFoICoordinates(url, coords):
    newfeature = {
        "feature": {
            "type": "Point",
            "coordinates": coords
        }
    }
    
    PATCHRequest(url, json.dumps(newfeature))


# In[ ]:




