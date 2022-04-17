#print all true
k=[1,2,4,5]
print(all(k))

#all false
k=[12,4,4,0]
print(all(k))

#one true
k=[0,False,5]
print(all(k))

#one false
k=[2,5,0]
print(all(k))

#iterable
k=[]
print(all(k))