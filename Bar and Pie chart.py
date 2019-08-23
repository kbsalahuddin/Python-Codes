#pets.txt
'''Dog 10
Cat 9
Raccon 5
Butterfly 6.5
Parrot 8
Goldfish 7.5'''

#pie and barchart from txt file data
import pygal

piechart=pygal.Bar()
piechart1=pygal.Pie()
file=open('pets.txt','r')
for line in file.read().splitlines():
  if line:
    label,value=line.split(' ')
    piechart.add(label,float(value))
    piechart1.add(label,float(value))
  #print(line)
file.close()  
piechart.title='Our Favourite Pets'
piechart.render_to_file('a.svg')
piechart1.render_to_file('a1.svg')