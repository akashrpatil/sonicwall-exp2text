# SonicWall EXP to TXT Converter

A Python 3 script to convert SonicWall `.exp` configuration backup files to a readable `.txt` format.

## Features
- Decodes Base64 `.exp` files.
- Converts the output to Windows-compatible linefeeds.
- Provides sample output for verification.

## Prerequisites
- Python 3.x
- `sed` (for Windows linefeed conversion, available on Linux/macOS)

## Installation
Clone the repository:
```
sh
git clone https://github.com/yourusername/sonicwall-exp2text.git
cd sonicwall-exp2text
```

**Usage**
Run the script with the default export.exp file:
```
python3 sonicwall-exp2text.py
```
**Or specify a custom .exp file:**
sh
Copy
Edit
```
python3 sonicwall-exp2text.py mybackup.exp
```
**Example Output**
```
--------------------------
Current File Defaults:
outputFile = ./export.txt
inputFile  = ./export.exp
--------------------------

* Decoding EXP file "export.exp".
* Text file "export.txt" created.
* Converting to Windows linefeeds using: "sed -i 's/&/\r\n&/g' ./export.txt"

Conversion completed.

Sample of export.txt:
...
```

**Removing Old Export Files**
If an old export file exists, the script will automatically remove it before creating a new one.

## Original Author  
- **Brady Shea**  
- GitHub: [bmatthewshea](https://gist.github.com/bmatthewshea)  
- Original Script: [Gist Link](https://gist.github.com/bmatthewshea/c038a0d38ce8804ac6eae39ae8f814f3)  

## Updated By  
This script has been **upgraded to Python 3** while maintaining the original functionality.
