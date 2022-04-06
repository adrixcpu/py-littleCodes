'''
Una función que reciba un número y un listado de números (en ese orden)
 y devuelva True si el número pertenece a la lista. Si el número no se encuentra presente, 
 la función debe incluirlo al final de la lista y devolverla.
'''

def check(x,y):
    if x in y:
        return True
    else:
        y.append(x)
        return y

milista = [1,2,3,4,5,6,4,6,4,7,8]
var = check(0,milista)
print(var)