#!/bin/bash

echo "$PWD"
sudo PYTHONPATH="$PYTHONPATH:$PWD" python3 src/main.py