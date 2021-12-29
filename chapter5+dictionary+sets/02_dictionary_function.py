myDictinary={
    "Name":"asif",
    "status":"Quick programmer",
    "List":[4,5,3,2,6],
    "AnotherDic":{'asif':"asif is a quick programmer"},

}
print(list(myDictinary.values())) #get the values of dic and convert it in list
print(myDictinary.keys())  #get the keys of dictinary
print(myDictinary.items())  #get the keys and values both of dictinary
updateDic={
    "name":"saqi"
} 
print(myDictinary)
print(myDictinary.update(updateDic))
print(myDictinary)

print(myDictinary.get('name')) 
print(myDictinary["name"])

print(myDictinary.get('name2')) # it will return none because name2 key is not present in dictionary
print(myDictinary["name2"]) #it will throws and error bcs name2 is not present in dic