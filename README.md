# Enhancing Data Security with ShiftCipher

# Caesar Cipher Algorithm

The Caesar Cipher is one of the simplest and most well-known encryption techniques. Named after Julius Caesar, who reportedly used it to communicate with his officials, this algorithm works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on. This method is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## How It Helps in Encryption and Decryption

### Encryption
To encrypt a message using the Caesar Cipher, you choose a shift value and apply it to each letter of the plaintext. This transforms the original message into an encoded one that appears meaningless to anyone who doesn't know the shift value. For instance, with a shift of 3, the word "HELLO" would be encrypted as "KHOOR".

### Decryption
Decryption is the reverse process of encryption. By knowing the shift value, you can shift the letters in the encoded message back by the same number of positions to reveal the original plaintext. Using the previous example, "KHOOR" with a shift of 3 would be decrypted back to "HELLO". This simple yet effective method ensures that the message remains confidential as long as the shift value is kept secret.

# Steps for execution

### Install python on any linux based system like "Kali Linux".
### To install python on kali linux use command
1. sudo apt update
2. sudo apt install python3 -y
### Open a text editor to create the script file. Use 'nano' or any other text editor available in Kali Linux
3. nano caesar_cipher.py
### write Caesar Cipher program code in text editor.
### Save the file 
4. Press 'CTRL+O' to save.
5. Hit 'Enter' to confirm the file name.
6. Press 'CTRL+X' to exit the editor.
### Run the code/script
7. python3 caesar_cipher.py
### Use the program
8. Enter a message to encrypt or decrypt when prompted (for eg: encrypt)
9. Enter shift value
10. Choose mode (encrypt/decrypt)
11. Enter yes/no to proceed further (for eg: to decrypt type 'yes')
12. Enter that encrypted message again
13. Enter same shift value given before
14. Choose mode (Encrypt/Decrypt)
15. If decrypted, entered message will be displayed which is taken by user as input.
16. Hence, same message is encrypted and as well as decrypted.
### This is a simple process that takes place in cryptography

