def decode_caesar_cipher(text, shift):
    decoded_text = ""
    for character in text:
        if character.isalpha():  # Check if the character is an alphabet
            shift_amount = shift % 26  # Ensure shift is within the alphabet range
            if character.islower():
                # Shift lowercase characters
                decoded_text += chr((ord(character) - 97 - shift_amount) % 26 + 97)
            else:
                # Shift uppercase characters
                decoded_text += chr((ord(character) - 65 - shift_amount) % 26 + 65)
        else:
            # Leave non-alphabet characters unchanged
            decoded_text += character
    return decoded_text

ciphertexts = ['iyemkx', 'aypjr', 'vxlg', 'krwjarnb', 'kwhv', 'XIBP', 'zevmefpiw!']
shifts = [16, 19, 23, 17, 12, 18, 22]

all = ''
for ct, shift in zip(ciphertexts, shifts):
    plain_txt = decode_caesar_cipher(ct, 26 - shift)
    all += plain_txt + " "
    print(shift, ct, ' = ', plain_txt)
    
print(all)
    