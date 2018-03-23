# Python-Affine-Cipher-Script
Useful for Affine / Monoalphabetic substitution cipher solving in Discrete Mathematics.

## Usage:

Run locally only using Python Interpreter. Example:
```
python affine-cipher-script.py
```

The script will first ask for the original message; spaces and case do not matter. Example: 
```
Enter message to cipher: flat BROKE
```

Next, the script will ask you for the cipher formula using the letter c as the variable. Example: 
```
Enter cipher formula using 'c' as the variable (all else should be operators and integers): (c + 13) % 26
```

The final result is displayed in lower case and the script terminates.
```
The result is: syng oebxr
```
