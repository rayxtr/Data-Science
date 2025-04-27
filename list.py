#Create a list
list = [1,2,4,5,7,8,9]
#Read a list
print(list[2])

print(list[-2])

#update a list
list[0]=3;

# add 
list.append('value')


list.insert(2,'Here')  # 2 is index and value placed

print(list)
a = list.copy()  # copy a list
print(a)

print(list.pop())  # Remove a value from top
list.clear()  # Clear a list.
print(list)
#a.remove(11) Remove a value 


#del(a); # Completely Delete a list
a.remove('Here')
a.remove('value')
print(len(a))
a.sort() # sort a list.
c = sorted(a)  #Create a another list which is sorted. 
print(c)
# if any list has mix datatype elements 
b =  [1,2,3,'m','j',0.2,0.7,8,7]

num = [x for x in b if isinstance(x, (int, float))]
stri = [x for x in b if isinstance(x,str)]

final = num+stri
print(final)

final.reverse()
print(final)



