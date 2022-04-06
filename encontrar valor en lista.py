'''Escribí una función que reciba una lista de números enteros y devuelva 
la cantidad de veces que aparece el número 4 en ella.'''

def cuenta_cuatro(milista):
    cont = milista.count(4)
    return cont

milista = [1,2,3,4,5,6,4,6,4,7,8]
var = cuenta_cuatro(milista)
print(var)