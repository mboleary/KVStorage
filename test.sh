#!/bin/bash

# Testing script for kv

python3 kv.py -h
python3 kv.py test.json -k
python3 kv.py test.json -w test 5
python3 kv.py test.json test
python3 kv.py test.json -s "tes*"


