#!/usr/bin/env python

import json
import yaml

def to_dict(fileName):
    f = open(fileName)
    dataMap = yaml.load(f)
    f.close()
    return dataMap

def to_json(dict):
    dict = json.dumps(dict)
    jsonOutput = json.loads(dict)
    return jsonOutput   
