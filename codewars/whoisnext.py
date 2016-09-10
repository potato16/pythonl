def whoIsNext(names, r):
 i=0
 s=0
 while True:
  tmp =s
  print(tmp,i)
  s+=5*2**i
  if r<s :
   s1= (r-tmp)//2**i
   s2= (r-tmp)%2**i
   
   if s2==0:
    return names[s1-1]
   else:
    return names[s1]
   break
  i +=1
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(whoIsNext(names,1802))
