# TransformTree

A python utility to transform a yaml file content with a specific structure to print another structure in json format.

### Usage

```
python3 transformTree.py
```
### Project Structure

```
- transformTree.py
  - build_groupwise_host_info function
- files
  - __init__.py
  - parser.py
    - to_dict function
    - to_json function
- resources
  - input.yaml  
```


### Input Sample:

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

### Output Sample:

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
        "vars": {
          "var1": 123,
          "var2": 456
        }
      },
      "node2.project1.datacenter1.dev.com": {
        "vars": {
          "var1": 123,
          "var2": 456
        }
      }
    }
  }
}

```