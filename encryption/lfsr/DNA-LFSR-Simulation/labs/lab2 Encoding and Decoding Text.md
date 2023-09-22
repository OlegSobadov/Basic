## Lab 2: Encoding and Decoding Text
### Objective: 
- Understand the translation between textual data and binary sequences suitable for LFSR processing.

### Initialization:

- Introduce ASCII and its role in character encoding.
### Tasks:

- Write a program that converts a given text string into its binary representation.
- Process this binary data using a basic LFSR (from Lab 1).
- Convert the processed binary data back into text.
### Evaluation:

- Discuss the differences between the original and processed texts.
- Reflect on the importance of encoding and decoding mechanisms.
---
Terminal Activity:

- Open your terminal.

Launch the Python interpreter:

```bash
$ python
```
Write functions to convert text to binary and vice-versa:
```bash
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
```
Test these functions:
```py
encoded = text_to_binary("HELLO")
print(encoded)

decoded = binary_to_text(encoded)
print(decoded)
```