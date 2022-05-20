import json
import yaml
import sys
import os

in_file = sys.argv[1]
out_file = sys.argv[2]

if os.path.exists(sys.argv[2]):
    print("ERROR: " + sys.argv[2] + " already exists")
    exit(1)

filename, file_extension = os.path.splitext(in_file)
if file_extension == '.json' or file_extension == '.jsn':
    with open(in_file, 'r') as json_in, open(out_file, "w") as yaml_out:
        json_payload = json.load(json_in)
        yaml.dump(json_payload, yaml_out, sort_keys=False)

elif file_extension == '.yml' or file_extension == '.yaml':
    with open(in_file, 'r') as yaml_in, open(out_file, "w") as json_out:
        yaml_payload = yaml.safe_load(yaml_in) 
        json.dump(yaml_payload, json_out, sort_keys=False)
else : 
    print("Error: Pass only json or yaml files")

