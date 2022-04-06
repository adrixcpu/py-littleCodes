'''
Escribí una función que tome una lista y devuelva True si hay dos números iguales, y False si son todos distintos.
'''

from multiprocessing.reduction import duplicate


def repetidos(x):
    norepite = set(x)
    if len(x)>len(norepite):
        return True
    else:
        return False
        
    

milista = [1,2,4,6,2,248,9,10]
var = repetidos(milista)
print(var)

