# empty dict creation

myDict={}
print(type(myDict))

# inserting key-value pairs
# NOte : items(whole pair), keys and values 
# the values, keys in dict can be of any datatype

myDict['a']=1
myDict['b']=2
myDict['c']='Ayush'
myDict['d']=4
myDict['e']={5,10,51}
myDict['f']=6
myDict['g']=7
myDict['h']=8

print(myDict)

# Dict are Ordered (sorted by keys) 
# No duplicates allowed also

myDict['h']=195370
print(myDict)

# adding a duplicate key will override the previous one

#-------------------------------------------------------------------------------------
# Dict Methods -> get(key), pop(key), popitem(), items(), values(), keys() 

# get(key) --> get the item with the key 'key'
# pop(key) --> pops the item with the key 'key'
# popitem() --> pops the last inserted key-value pair

myDict.popitem()
print(myDict)

print(myDict.get('c'))

myDict.pop('c')
print(myDict)

print(myDict.values())
print(myDict.keys())