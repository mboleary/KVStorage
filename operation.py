# Operation Class
# 
# Defines what to perform onto the JSON File, so that operations can be performed in a certain order

from enum import Enum

import sys

# We only have specific operations to perform
class Op(Enum):
    VIEW = 1
    ADD = 2
    DELETE = 3
    VIEW_KEYS = 4
    SEARCH_KEYS = 5
    NOP = 0

def genOperation(arg, key, val):
    if arg == "-v":
        return Operation(Op.VIEW, key, "")
    elif arg == "-w":
        return Operation(Op.ADD, key, val)
    elif arg == "-d":
        return Operation(Op.DELETE, key, "")
    elif arg == "-s":
        return Operation(Op.SEARCH_KEYS, key, "")
    elif arg == "-k":
        return Operation(Op.VIEW_KEYS, key, "")
    else:
        print("Invalid Operation:", arg, file=sys.stderr)

class Operation:
    op = Op.NOP
    key = ""
    value = ""

    def __init__(self, op, key, value):
        self.op = op
        self.key = key
        self.value = value

    # Do the operation on the JSON Object
    # @return: Returns anything to be printed
    def do(self, j):
        if self.op == Op.VIEW:
            if self.key in j:
                print(j[self.key])
            else:
                print("")
        elif self.op == Op.ADD:
            j[self.key] = self.value
        elif self.op == Op.DELETE:
            if self.key in j:
                del j[self.key]
        else:
            print("Did Nothing!")