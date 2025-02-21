#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import os
import sys
import subprocess
import shlex

# Defaults
outputFile = './export.txt'
inputFile = './export.exp'
sed_args = f"sed -i 's/&/\\r\\n&/g' {outputFile}"
head_args = f"head {outputFile}"

print("\n--------------------------")
print("Current File Defaults:")
print(f"outputFile = {outputFile}")
print(f"inputFile  = {inputFile}")
print("--------------------------\n")

# Remove old conversion file if found
if os.path.exists(outputFile):
    print(f'* Found previous text export file.\n* Removing old file: {outputFile}\n')
    os.remove(outputFile)

# Check if a custom input file is provided
if len(sys.argv) == 1:
    print(f"* No EXP file found on command line.\n* Using default ({inputFile}) as input filename.\n")
else:
    inputFile = sys.argv[1]

# Decode Base64 file
print(f'* Decoding EXP file "{inputFile}".')

try:
    with open(inputFile, "rb") as infile, open(outputFile, "wb") as outfile:
        base64.decode(infile, outfile)
except FileNotFoundError:
    print(f"Error: File '{inputFile}' not found. Exiting.")
    sys.exit(1)

# Convert linefeeds
print(f'* Text file "{outputFile}" created.\n* Converting to Windows linefeeds using: "{sed_args}"\n')
subprocess.call(sed_args, shell=True)

print("Conversion completed.\n")

# Show sample of new file
print(f"Sample of {outputFile}:\n")
subprocess.call(shlex.split(head_args))
print("\nExiting.")
sys.exit(0)
