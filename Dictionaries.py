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



inventory={
      "item1":100,
      "item2":200,
      "item3":300
}

inventory['item1']-=3
print(inventory['item1'])

if 'item4' not in inventory:
      inventory['item4']=345
      print(inventory)

text = "I am a multimillionare a boy"
word={}
# for w in text.split():
#       if w in word:
#             word[w]+=1
#       else:
#             word[w]=1
for w in text.split():
    word[w]=  word.get(w,0)+1
print(word)

new_d = dict.fromkeys(word.keys(),'')
print(new_d)
liss = [33,44,55,32]
dit = dict.fromkeys(liss,'yes')
print(dit)

