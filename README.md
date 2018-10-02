# TransformTree

A python utility to transform a yaml file content with a specific structure to print another specified structure in json format.

### User Acceptance Testing

```
python3 -m doctest -v test_inventory.txt
```

### Usage

```
python3 inventory.py
```
### Project Structure

```
- inventory.py
  - build_groupwise_host_info function
- parser.py
  - generate dict function
  - to_json function
- inventory
  - input.yaml  
```

### Input Sample to be present inventory/input.yaml:

``` 
hosts:
  node1.project1.datacenter1.dev.com:
    vars:
      var1: 123
      var2: 456
    groups:
      - test
      - datacenter1
      - dev
      
  node2.project1.datacenter1.dev.com:
    vars:
      var1: 123
      var2: 456
    groups:
      - test
      - datacenter1
      - dev

```      

### Output Sample generated:

```
{
  "test": {
    "hosts": [
      "node1.project1.datacenter1.dev.com",
      "node2.project1.datacenter1.dev.com"
    ]
  },
  "datacenter1": {
    "hosts": [
      "node1.project1.datacenter1.dev.com",
      "node2.project1.datacenter1.dev.com"
    ]
  },
  "dev": {
    "hosts": [
      "node1.project1.datacenter1.dev.com",
      "node2.project1.datacenter1.dev.com"
    ]
  },
  "_meta": {
    "hostvars": {
      "node1.project1.datacenter1.dev.com": {
        "var1": 123,
        "var2": 456
      },
      "node2.project1.datacenter1.dev.com": {
        "var1": 123,
        "var2": 456
      }
    }
  }
}

```

