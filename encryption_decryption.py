enc_or_dec = input("Enter '1' for encyrpt and '2' for decrypt: ")
text = input("Enter word to encrypt or decrypt: ").lower()
shift = int(input("Enter shift number "))
new_text = ""
if enc_or_dec == "1":
    for character in text:
        a = ord(character) + shift
        if a > 122:
            a = (a % 122) + 96
        new_text += chr(a)
    print(new_text)
elif enc_or_dec == "2":
    for character in text:
        i = ord(character) - shift
        if i < 97:
            i = 123 - (97 % i)
        new_text += chr(i)
    print(new_text)
