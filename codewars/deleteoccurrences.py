def delete_nth(order,max_e):
 neworder =[]
 dicor={}
 for i in order:
  if i not in dicor:
   dicor[i]=1
   neworder.append(i)
  else:
   if dicor[i]< max_e:
    neworder.append(i)
    dicor[i]+=1
 print(neworder)
 return neworder
    # code here
delete_nth([20,37,20,21], 1)
