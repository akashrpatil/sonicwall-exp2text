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
```sh
git clone https://github.com/yourusername/sonicwall-exp2text.git
cd sonicwall-exp2text

Usage
Run the script with:

sh
Copy
Edit
python3 sonicwall-exp2text.py
Or specify a custom EXP file:

sh
Copy
Edit
python3 sonicwall-exp2text.py mybackup.exp
Example Output
arduino
Copy
Edit
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
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

License
MIT License

yaml
Copy
Edit

---

## **Git Commands to Upload to GitHub**
### **Step 1: Initialize a Git Repository**
If you haven’t initialized a Git repository yet, run:
```sh
git init
Step 2: Add Your Files
sh
Copy
Edit
git add sonicwall-exp2text.py README.md
(Optional: Add a .gitignore file to exclude unnecessary files like .DS_Store or __pycache__/.)

Step 3: Commit Your Changes
sh
Copy
Edit
git commit -m "Initial commit - SonicWall EXP to TXT Converter"
