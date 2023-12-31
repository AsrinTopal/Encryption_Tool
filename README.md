# Encryption and Decryption Tool

## Introduction
Welcome to the Encryption and Decryption Tool, a Python-based program aimed to provide a reliable, secure, and easy-to-use solution for encoding and decoding textual data. In an era where data security is critical, this application distinguishes itself by including the widely used base64 encoding technology as well as a key-based security mechanism, all wrapped within an easy-to-use graphical user interface (GUI).

## Approach
The application uses the base64 encoding technique for both encryption and decryption. The key is required to access the encrypted content. The GUI provides a user-friendly interface to input text and the secret key.

## Memory and Time Complexity
### Overall Complexity
- Memory Complexity: O(n)

    The overall memory complexity is dominated by the size of the input text during both encryption and decryption processes.

- Time Complexity: O(n)

    The overall time complexity is linear, primarily influenced by the size of the input text during encoding and decoding operations.

- Considerations

    Because of the effectiveness of the base64 encoding approach, the tool is well-suited for handling tiny to medium-sized documents.
    Key operations' continuous time and memory complexity add to the overall efficiency of the encryption and decryption procedures.
    These complexity evaluations shed light on the Encryption and Decryption Tool's scalability and efficiency for varied input sizes.
## Installation
1. Clone the repository:   
```bash
git clone https://github.com/AsrinTopal/Encryption_Tool.git
cd Encryption_Tool
```
## Install the required dependencies:
```bash
pip install tk
```
AND 
```bash
pip install pybase64
```

# Important Code Parts

### Encryption

Encryption Process
The application employs the widely-used base64 encoding technique for encrypting text. During encryption, the user inputs a piece of text into the application's graphical user interface (GUI). This text undergoes a two-step process:

1-ASCII Encoding 

2-Base64 Encoding

```python
#Relevant code for encryption
encode_message = message.encode("ascii")
base64_bytes = base64.b64encode(encode_message)
encrypt = base64_bytes.decode("ascii")
```
The resulting output, encrypt, is the encrypted form of the original text.
#
### Decryption
To decrypt the encrypted content, a user needs to provide the correct key. The decryption process involves the following steps:

1-Base64 Decoding

2-ASCII Decoding
```python
#Relevant code for decryption
decode_message = message.encode("ascii")
base64_bytes = base64.b64decode(decode_message)
decrypt = base64_bytes.decode("ascii")
```

The decrypt variable now holds the decrypted text, which was originally encrypted using the same application.
#
**The default password is 1234 you can change it if you want, in the encryption and decryption part.** 
```python
password == "1234":
```
#
#### Key Requirement
A secret key is necessary for both encryption and decryption. This key is used to get access to and change the material. The user is prompted to enter this key, ensuring a safe and restricted access method.
#
#### User-Friendly GUI
The graphical user interface of the program is intended to improve the user experience. It provides an easy-to-use platform for users to enter text and keystrokes. The simple design guarantees that users may simply encrypt and decode files without having to deal with additional complexity. The GUI helps to make the encryption and decryption operations more accessible to people with a variety of technical backgrounds.

[![main](https://i.postimg.cc/Gm9t6Btj/image-2023-12-29-225723502.png)](https://postimg.cc/QFGjTdpB)
[![emain](https://i.postimg.cc/L8Tdkv2C/image-2023-12-29-225919064.png)](https://postimg.cc/LJn02tqL)
[![encrypt](https://i.postimg.cc/50ysCS2C/image-2023-12-29-225828434.png)](https://postimg.cc/WFRmRrrN)
[![decrypt](https://i.postimg.cc/9Xqvgccq/image-2023-12-29-225953769.png)](https://postimg.cc/7bwsf8Gx)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
