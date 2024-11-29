# Caesar Cipher Implementation
# This program allows users to encrypt or decrypt messages using the Caesar Cipher technique.

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Function to perform Caesar Cipher encryption or decryption.
    Args:
        text (str): The input text to encrypt or decrypt.
        shift (int): The number of positions to shift each letter.
        mode (str): Mode of operation, either 'encrypt' or 'decrypt'.
    Returns:
        str: The resulting encrypted or decrypted text.
    """
    # Initialize the result string
    result = ""
    
    # Adjust shift value for decryption mode
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption
    
    # Process each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base ASCII value (A for uppercase, a for lowercase)
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Non-alphabet characters are added as is
            result += char  
    
    # Return the final encrypted or decrypted text
    return result

# Initial welcome message
print("Welcome to the Caesar Cipher Program!")

# Main loop to allow multiple rounds of encryption or decryption
while True:
    # Get the message to encrypt or decrypt
    text = input("Enter the message: ")
    
    # Get the shift value from the user
    shift = int(input("Enter the shift value: "))
    
    # Ask the user to choose the mode (encrypt or decrypt)
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    
    # Check if the user selected a valid mode
    if mode in ['encrypt', 'decrypt']:
        # Perform the encryption or decryption
        output = caesar_cipher(text, shift, mode)
        
        # Display the result
        print(f"The {mode}ed message is: {output}")
        
        # Ask the user if they want to continue with the new output message
        continue_choice = input("Do you want to encrypt/decrypt this result again? (yes/no): ").strip().lower()
        
        # Exit the program if the user chooses 'no'
        if continue_choice == 'no':
            print("Exiting the program.")
            break
        else:
            # Use the encrypted or decrypted message as the new input for the next round
            text = output
    else:
        # Notify the user about invalid mode selection
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
