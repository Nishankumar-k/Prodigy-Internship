def caesar_cipher():
    while True:
        print(" Welcome to Caesar Cipher Encoder/Decoder \n")
        print("1. Encode ")
        print("2. Decode ")
        print("3. Exit ")
        print("Enter your option for operations: \n")
        option = int(input())
        if option == 1:
            print("Enter text to be encoded: ")
            text = input()
            print("Enter shift value: ")
            shift = int(input())
            encoded = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = 97 if char.islower() else 65
                    encoded += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    encoded += char
            
            print("The encoded text is: " + encoded)

        elif option == 2:
            print("Enter Encrypted Text to be decoded: ")
            text = input()
            print("Enter shift value: ")
            shift = int(input())
            decoded = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = 97 if char.islower() else 65
                    decoded += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    decoded += char
            
            print("The decrypted text is: " + decoded)

        elif option == 3:
            exit()
        
        else:
            print("Invalid option. Please try again. \n")

if __name__ == "__main__":
    caesar_cipher()
