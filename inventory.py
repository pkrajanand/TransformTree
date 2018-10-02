#!/usr/bin/env python

import parser

def build_groupwise_host_info(input_data):
  nodes = input_data['hosts']
  groups_to_nodes_tree = build_groups_to_nodes_tree(nodes)    
  host_vars = build_host_vars_subtree(nodes) 
  groups_to_nodes_tree["_meta"] = host_vars
  return groups_to_nodes_tree

def build_groups_to_nodes_tree(nodes):
  groups_to_nodes_tree = {}
  for node_name, node_details in nodes.items():
    for group_name in node_details['groups']:
      if group_name in groups_to_nodes_tree:
        groups_to_nodes_tree[group_name]["hosts"].append(node_name) 
      else:    
        groups_to_nodes_tree[group_name] = {"hosts": [node_name]}
  return groups_to_nodes_tree

def build_host_vars_subtree(nodes):
  node_vars = {}
  host_vars = {"hostvars": {}}
  for node_name in list(nodes):
    del nodes[node_name]['groups']
    for k,v in nodes.items():
      if v.__contains__('vars'):
        for x,y in v.items():
          node_vars[k] = y
  host_vars["hostvars"] =  node_vars
  return host_vars

def main():
  input_data = parser.generate_data()
  groupwise_host_info = build_groupwise_host_info(input_data)
  jsonOutput = parser.to_json(groupwise_host_info)
  print(jsonOutput)

main()