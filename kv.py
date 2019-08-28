#!/usr/bin/python3

# Key/Value Pair from JSON in Javascript

import json
import sys
import os

from operation import Op, Operation, genOperation

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
printJSON = False
operations = []

def main():
    parseArgs()

    pass

# Parse Arguments
def parseArgs():
    key = ""
    value = ""
    currFlag = ""
    getKeyNext = False
    getValueNext = False
    procArg = False # True if the atom needs to be converted into an operation
    procAfterKey = False # True if processing should occur after reading the key
    procAfterValue = False # True if processing should occur after reading the value
    for i, a in enumerate(sys.argv):
        if i == 0:
            # Skip the Program Name
            continue
        elif i == 1:
            # This will be a command
            jsonFileName = a
            getKeyNext = True # Allow for View Shortcut
        elif i >= 2:
            if getKeyNext:
                # Special Case: Optionally have a flag or the filename.json
                if i == 1 and a == "-v":
                    getKeyNext = True
                elif i >= 1:
                    key = a
                    getKeyNext = False
                    if procAfterKey:
                        procAfterKey = False
                        procArg = True
            elif getValueNext:
                value = a
                getValueNext = False
                if procAfterValue:
                    procAfterValue = False
                    procArg = True
            else:
                # Parse a Command Flag
                currFlag = a

                # Always get only Key: -v -d -s
                if a == "-v" or a == "-d" or a == "-s":
                    getKeyNext = True
                    procAfterKey = True
                # Sometimes get only Key: -k
                elif a == "-k":
                    # Check next arg to determine if there is a key
                    if i + 1 < len(sys.argv) and sys.argv[i].find("-") != -1:
                        # There is a key
                        getKeyNext = True
                        procAfterKey = True
                    else:
                        # No Key
                        procArg = True
                # Get both a Key and a Value
                elif a == "-w":
                    getKeyNext = True
                    getValueNext = True
                    procAfterValue = True
        # Process the argument, but only when it's ready
        if procArg:
            procArg = False
            print("Parsed Operation", currFlag, key, value)
            operations.append(genOperation(currFlag, key, value))
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
