#The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a 
#certain number of places in the alphabet. We call the length of shift the key. 
#For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift 
#the encrypted letters in the opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.

try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Siberian Husky')
print('The Caesar cipher encrypts letters by shifting them over by a key number.')
print('For example, a key of 2 means the letter A is encrypted into C, the letter B encrypted into D, and so on.')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response = input('>> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter letter e for encrypt or d for decrypt')
    
while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use'.format(maxKey))
    response = input('>> ').upper()
    
    if not response.isdecimal():
        continue
    
    if 0 <= int(response) <= len(SYMBOLS):
        key_number = int(response)
        break
    
print('Enter the message to {}'.format(mode))
message = input('>> ')

# Caesar cipher only works on uppercase letters
message_mode = message.upper()

translated = ''

for symbol in message_mode:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num += key_number
        elif mode == 'decrypt':
            num -= key_number
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        translated = translated + SYMBOLS[num]
        #print(translated)
    else:
        translated = translated + symbol
        
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass  # Do nothing if pyperclip wasn't installed

#MJQQT BTWQI!