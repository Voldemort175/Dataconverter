# Dataconverter
Can convert files from JSON to YAML format and vice versa

## Installation

This script requires Python to be installed on the local machine. Please visit Python.org to install or type python3 --version to verify if it is already installed.

Once Python is installed, clone the project or download the ZIP file and extract manually.

## Build
You need to check whether PyYAML and simplejson are already installed in you system. 
If not,in your terminal Run : 
```
pip install pyyaml 
```
and 
```
pip install simplejson
```

## Usage 
Place a JSON or YAML file within the same directory as the script.

Navigate to the directory where the script exists.

1)If you want to convert JSON to YAML:
In the terminal, run: 
```python3 dataconverter.py ex1.json ex2.yaml```

where ex1 is the json file on your system and ex2 is a new file to be created after converting to yaml format.





2)If you want to convert YAML to JSON:
In the terminal, run: 
```python3 dataconverter.py ex1.yaml ex2.json```

where ex1 is the yaml file on your system and ex2 is a new file to be created after converting to json format.


If the converted filename exists, an error message will pop up.


