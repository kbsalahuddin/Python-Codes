myname=input('Your name:')
frname=input('Your friend\'s name:')
score=25
vowels1=0
vowels2=0

if len(myname)==len(frname):
  score=score+30
if (len(myname)+len(frname))>9:
  score=score+25.5
  
for i in myname:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels1=vowels1+1
print("Number of vowels are:",vowels1)


for i in frname:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels2=vowels2+1
print("Number of vowels are:",vowels2)

if (vowels1+vowels2)>=4:
  score=score+25
  
if score>90:
  print('Your friendship result:',score,'Besties :)')
else:
  print('Your friendship result:',score)