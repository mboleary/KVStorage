# Operation Class
# 
# Defines what to perform onto the JSON File, so that operations can be performed in a certain order

from enum import Enum

# We only have specific operations to perform
class Op(Enum):
    VIEW = 1
    ADD = 2
    DELETE = 3
    NOP = 0

class Operation:
    op = Op.NOP
    key = ""
    value = ""

    def __init__(self, op, key, value):
        self.op = op
        self.key = key
        self.value = value

    # Do the operation on the JSON Object
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