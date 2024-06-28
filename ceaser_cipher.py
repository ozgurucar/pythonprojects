alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = str(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))

if (direction == 'encode'):
    def encrypt(text, shift):
        final_text = ""
        size = len(text)
        for i in range(size):
            final_text += alphabet[(alphabet.index(text[i]) + shift) % 26]
        print(f"Encrypted text: {final_text}")


    encrypt(text, shift)

if (direction == 'decode'):
    def decrypt(text, shift):
        final_text = ""
        size = len(text)
        for i in range(size):
            bound_check = (alphabet.index(text[i]) - shift)
            if bound_check >= 0:
                final_text += alphabet[bound_check]
            else:
                final_text += alphabet[bound_check + 26]
        print(f"Decyrpted text is : {final_text}")


    decrypt(text, shift)
