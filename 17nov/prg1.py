#prg for nested disctionary
products={
    1:{"code":1,"name":"printer","price":20000},
    2:{"code":2,"name":"pendrive","price":500},
    3:{"code":3,"name":"moniterprinter","price":3000},
}
print(products)
products[1]["code"]=101
print(products)
products[3]["price"]=12000
print(products)