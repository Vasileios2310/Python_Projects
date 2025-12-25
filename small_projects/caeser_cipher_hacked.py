#This program can hack messages encrypted  with the Caesar cipher, even if you don’t know the key. 
# There are only 26 possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user.
# In cryptography, we call this technique a brute-force attack.


print('Caesar Cipher Hacker, by Siberian Husky')
print()

print('Enter the encrypted Caesar cipher message to hack')
message = input('>> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#symbols_lower = SYMBOLS.lower()


for key in range(len(SYMBOLS)):
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            
            if num < 0:
                num = num + len(SYMBOLS)
                
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
            
    print('Key #{}: {}'.format(key, translated))