
data = input("Enter text for encrypt: ")
def encrypt(data):
    encrypted_text = ''
    for c in data:
        charvalue = ord(c)
        character = (charvalue + 13)

        if(charvalue >= 65 and charvalue<= 90):
            if character > 90:
                character = (character % 90) + 64
        elif(charvalue >= 97 and charvalue <= 122):
            if character > 122:
                character = (character % 122) + 96
        else:
            return           
        encrypted_text += chr(character)
    print('Encrypted Text : ' + encrypted_text)              
encrypt(data)