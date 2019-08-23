
alphabet='abcdefghijklmnopqrstuvwxyz'
key1=input('Enter an integer key value:')
key=int(key1)
#encryption:

CryptChar=''
msg=input('Enter a Message (all alphabets must be in lowercase):')

for character in msg:
  position=alphabet.find(character)
  #print(position)

  encPosition=(position+key) % 26
  #print(encPosition)

  encChar=alphabet[encPosition]
  #print('The new message is:',encChar)
  #enter a to display d. b=1,c=2,d=3. so d will replace a.
  CryptChar += encChar
print('Your encrypted message is:',CryptChar)

#decryption:
dd=input('Do you also want decrypt the message?(Y/N)')
if dd=='Y' or dd=='y':
  DecryptChar=''
  for character1 in CryptChar:
    position1=alphabet.find(character1)
    decPosition=(position1-key)%26
    decChar=alphabet[decPosition]
    DecryptChar += decChar
  print('Real Messeage was:',DecryptChar)  
else:
  print('Okay, Thank you!')
