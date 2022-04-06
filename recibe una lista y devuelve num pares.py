'''
Escribí una función que reciba una lista de números y devuelva los pares de esa lista. 
Si alguno de los números es el 248, la lista no debería incluirlo.
Por ejemplo:
Aplicar la función stop_248() a la lista [1,2,4,248,9,10] debería devolver como resultado la lista [2,4,10]
'''

def stop_248(x):
    new_list=[]
    for i in x:
        if (i%2)==0 and (i!=248):
            new_list.append(i)
    return new_list

milista = [1,2,4,6,8,248,9,10]
var = stop_248(milista)
print(var)