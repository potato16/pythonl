import pickle
shoplistfile= 'shoplist.data'
shoplist=['apple','mango','carrot']
#write to the file
f = open (shoplistfile,'wb')
#DUmp the object to a file
pickle.dump(shoplist,f)
f.close()
#Destroy the shoplist variable
del shoplist
#Read back from the storage
f = open(shoplistfile,'rb')
storedlist=pickle.load(f)
print(storedlist)
