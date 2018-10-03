#!/usr/bin/env python

import json
import yaml
import glob

def generate_data():
  tmp_dict = {}
  files = glob.glob('inventory/*.yaml')
  for yaml_files in files:
    with open(yaml_files) as fd:
      data = yaml.load(fd)
      del data['groups']
    for k,v in data.items():
      tmp_dict.update(v)
  data['hosts'] = tmp_dict
  return data

def to_json(convert_to_json):
  result = json.dumps(convert_to_json, sort_keys=True)
  return result