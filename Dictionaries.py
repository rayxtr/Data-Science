#store data in key-value pair , key immutable unique, value can be mutable duplicates

#Create
dc = {
    1:'ankit',
    2:'rahul',
    3:'aditi',
    4:'anjali'
}
#Read
print(dc[1]) # get value of key
print(dc.keys())  #get all keys
dc.values() # get all values

se ={}
lis = [2,3,4,4,5,4,3,7,8]

fe={}

for x in range(len(lis)):
        fe[100+x]= lis[x]
        
print(fe)
for k , v in fe.items():
      print(k,'---',v)
for x in lis:
    se[x]=se.get(x,0)+1



print(se)
