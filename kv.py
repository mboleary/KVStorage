#!/usr/bin/python3

# Key/Value Pair from JSON in Javascript

import json
import sys
import os

import Op, Operation from operation

# if len(sys.argv) < 3:
# 	print("Usage: kv.py <file.json> key");
# 	sys.exit(1)
# path = sys.argv[1]
# if os.path.isfile(path):
# 	f = open(path)
# 	j = json.loads(f.read())
# 	f.close()
# 	key = sys.argv[2]
# 	# Check if we are saving
# 	if len(sys.argv) == 5:
# 		j[key] = sys.argv[4]
# 		f = open(path, 'w')
# 		f.write(json.dumps(j))
# 		f.close()
# 	else:
# 		if key in j:
# 			print(str(j[key]))
# else:
# 	if len(sys.argv) == 5:
# 		j = {}
# 		key = sys.argv[2]
# 		j[key] = sys.argv[4]
# 		f = open(path, 'w')
# 		f.write(json.dumps(j))
# 		f.close()

# Flags and variables from parsing
saveChanges = False
jsonContents = {}
jsonFileName = ""
key = ""
value = ""
printJSON = False
operations = []

def main():
    parseArgs()
    pass

# Parse Arguments
def parseArgs():
    getKeyNext = False
    getValueNext = False
    for a, i in sys.args:
        if i == 0:
            continue
        elif i == 1:
            jsonFileName = a
            getKeyNext = True
        elif i >= 2:
            if getKeyNext:
                # Special Case: Optionally have a flag or the filename.json
                if i == 1 and a == "-v":
                    getKeyNext = True
                elif i > 1:
                    jsonFileName = a
                getKeyNext = False
            elif getValueNext:
                value = a
                getValueNext = False
    pass

# Load or Create the JSON File
def loadOrCreateFile():
    pass

# Save the Updated JSON
def saveFile():
    pass

# Performs all Operations
def doOps():
    pass

if __name__ == "__main__":
    main()
