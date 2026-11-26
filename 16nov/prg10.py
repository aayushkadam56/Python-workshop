# prg. for dictionary
product={"code":101,"name":"printer"}
print(type(product))
print(product)

#assignment operator
product["price"]=20000
print(product)

#updation
product["code"]=111
print(product)

#update() :- add new data in key+value format
product.update({"qty":2})
print(product)

#keys ():-- returns all keys of dictionary
print(product.keys())

#values():-- returns all values of dictionary
print(product.values())

#items():-- returns all keys of dictionary
print(product.items())

#pop():-- removes data on basis of key
product.pop("qty")
print(product)

#popitem():--removes last record of dictionary
product.popitem()
print(product)

#get():--returns key on basis of value
x=product.get("code")
print(x)

#copy():--
productnew=product.copy()
print(productnew)

productnew["qty"]=10
print(productnew)
print(product)

productnew.clear()
print(productnew)

productnew["productcode"]=101
productnew["name"]="moniter"
productnew["price"]=10000
print(productnew)
del productnew
print(productnew)