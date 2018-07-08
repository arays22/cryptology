plaintext = input('Enter your message: ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
k = 1
cipher = ''

for i in plaintext:
    if i in alphabet:
        cipher += alphabet[(alphabet.index(i) + k) % (len(alphabet))]

print('The encrypted message: ' + cipher)
