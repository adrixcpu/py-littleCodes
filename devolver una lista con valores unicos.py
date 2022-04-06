'''
Una función que reciba una lista y devuelva otra lista eliminando los valores repetidos
'''
def unicos(lista):
    nueva  = []
    for i in lista:
        if i not in nueva:
            nueva.append(i)
    return nueva 

milista = [1,2,4,6,2,248,9,10]
var = unicos(milista)
print(var)