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
hasWriteOp = False # True if a write operation is parsed. Used to determine whether to create a file

def main():
    global jsonFileName
    global operations
    global saveChanges

    parseArgs()
    # Load the file (If file doesn't exist, create only if there is a write operation)
    if os.path.isfile(jsonFileName) or hasWriteOp:
        loadOrCreateFile()
        # if print("File", jsonFileName, "loaded")
    else:
        # Whatever operation was going to be performed here would result in an empty string, so just exit.
        # print("File Not Loaded")
        sys.exit()

    doOps()

    if saveChanges:
        saveFile()
        # print("Changes Saved to File")

# Parse Arguments
def parseArgs():
    global jsonFileName
    global hasWriteOp
    global operations
    global saveChanges

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
            # print("ProgName:", a)
            continue
        elif i == 1:
            # This will be the JSON Filename
            # print("Filename:", a)
            jsonFileName = a
        elif i >= 2:
            if getKeyNext:
                # Special Case: Optionally have a flag or the filename.json
                # print("Getting Key:", a)
                key = a
                getKeyNext = False
                if procAfterKey:
                    procAfterKey = False
                    procArg = True
            elif getValueNext:
                
                # print("Geting Value:", a)
                value = a
                getValueNext = False
                if procAfterValue:
                    procAfterValue = False
                    procArg = True
            else:
                # Parse a Command Flag
                # print("Parsing Flag:", a)
                
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
                # Check for shortcut: View Name after JSON Filename
                elif i == 2:
                    # print("Special Case: View Shortcut")
                    key = a
                    currFlag = "-v"
                    procArg = True
        # Process the argument, but only when it's ready
        if procArg:
            procArg = False
            # print("Parsed Operation", currFlag, key, value)
            operations.append(genOperation(currFlag, key, value))
            if currFlag == "-w":
                hasWriteOp = True
                saveChanges = True
            elif currFlag == "-d":
                saveChanges = True
    if len(operations) == 0:
        print("Help should be printed here!")
        sys.exit()

# Load or Create the JSON File
def loadOrCreateFile():
    global jsonContents
    global jsonFileName
    try:
        if (os.path.isfile(jsonFileName)):
            f = open(jsonFileName)
            jsonContents = json.loads(f.read())
            f.close()
        else:
            jsonContents = {}
    except IOError as e:
        print("There was a problem opening the file.", e, file=sys.stderr)
        sys.exit()

# Save the Updated JSON
def saveFile():
    global jsonFileName
    global jsonContents

    try:
        f = open(jsonFileName, 'w')
        f.write(json.dumps(jsonContents))
        f.close()
    except IOError as e:
        print("There was a problem opening the file.", e, file=sys.stderr)
        sys.exit()

# Performs all Operations
def doOps():
    global operations
    global jsonContents
    while len(operations) > 0:
        op = operations.pop(0)
        op.do(jsonContents)
        # print("Performed Operation", op.op)
        # print("JSON:", jsonContents)

if __name__ == "__main__":
    main()
