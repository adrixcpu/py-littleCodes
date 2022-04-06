#compresion de listas

list_ejem =[{'id':1,'name':'juan','age':19},{'id':2,'name':'jose','age':24},{'id':3,'name':'maria','age':22},{'id':4,'name':'ana','age':18}]
print(list(e for e in list_ejem if e['id']  == 4)[0])
print(list(e for e in list_ejem if e['name']  == 'Juan')[0])

list(filter(lambda x: x["id"]==4, list_ejem))[0]
