#!/usr/bin/env python

import files.parser

def build_groupwise_host_info(_hosts_to_groups_tree):
    nodes = _hosts_to_groups_tree['hosts']
    _groups_to_nodes_tree = build_groups_to_nodes_tree(nodes)    
    _host_vars = build_host_vars_subtree(nodes)    
    _groups_to_nodes_tree["_meta"] = _host_vars
    return _groups_to_nodes_tree

def build_groups_to_nodes_tree(nodes):
    _groups_to_nodes_tree = {}
    for node_name, node_details in nodes.items():
        for _group_name in node_details['groups']:
            if _group_name in _groups_to_nodes_tree:
                _groups_to_nodes_tree[_group_name]["hosts"].append(node_name) 
            else:    
                _groups_to_nodes_tree[_group_name] = {"hosts": [node_name]}
    return _groups_to_nodes_tree

def build_host_vars_subtree(nodes):
    _host_vars = {"hostvars": {}}
    for node_name in list(nodes):
        del nodes[node_name]['groups']

    _host_vars["hostvars"] =  nodes   
    return _host_vars

def main():    
    _hostwise_groups_info = files.parser.to_dict('resources/input.yaml')
    _groupwise_host_info = build_groupwise_host_info(_hostwise_groups_info)
    jsonOutput = files.parser.to_json(_groupwise_host_info)
    print(jsonOutput)

main()