from random import choice
Strikers=['Auba','Laca','Nekieta']
Mids=['Mikhy','Ozil','Carzola','Xhaka','Ramsey','Wilshere']
Defs=['Kos','Hector','Nacho']
GKs=['Ben','Ospina','Cech']
#choice function only picks one at a time from a list
Team1=[]
Team2=[]
Team3=[]
while len(Strikers)>0:
  st=choice(Strikers)
  Team1.append(st)
  Strikers.remove(st)

  st=choice(Strikers)
  Team2.append(st)
  Strikers.remove(st)

  st=choice(Strikers)
  Team3.append(st)
  Strikers.remove(st)
while len(Mids)>0:
  mids=choice(Mids)
  Team1.append(mids)
  Mids.remove(mids)
  mids=choice(Mids)
  Team1.append(mids)
  Mids.remove(mids)
  
  mids=choice(Mids)
  Team2.append(mids)
  Mids.remove(mids)
  mids=choice(Mids)
  Team2.append(mids)
  Mids.remove(mids)
  
  mids=choice(Mids)
  Team3.append(mids)
  Mids.remove(mids)
  mids=choice(Mids)
  Team3.append(mids)
  Mids.remove(mids)
while len(Defs)>0:
  defs=choice(Defs)
  Team1.append(defs)
  Defs.remove(defs)
  
  defs=choice(Defs)
  Team2.append(defs)
  Defs.remove(defs)
  
  defs=choice(Defs)
  Team3.append(defs)
  Defs.remove(defs)
while len(GKs)>0:
  gks=choice(GKs)
  Team1.append(gks)
  GKs.remove(gks)
  
  gks=choice(GKs)
  Team2.append(gks)
  GKs.remove(gks)
  
  gks=choice(GKs)
  Team3.append(gks)
  GKs.remove(gks)
  
print("Team 1's five a side lineup is:",Team1)
print("Team 2's five a side lineup is:",Team2)
print("Team 3's five a side lineup is:",Team3)

