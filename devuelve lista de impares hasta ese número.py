'''
Una función que, dado un número, devuelva una lista 
con los los números impares comprendidos entre 0 y ese número (sin incluirlo). 
Como condición, la función se debe construir con una lista por comprensión.
##### nueva_lista = [expresion bucle_for condiciones]
print(results) = [2, 3, 4, 5]
##Por compresión sería
numbers = [1, 2, 3, 4]
results = [n + 1 for n in numbers]
'''

def impares(num):    
    lista=[ n for n in range(num) if n%2!=0]
    return lista

print(impares(7))
print(impares.lenght())
    