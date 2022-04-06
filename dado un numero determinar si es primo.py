'''
Escribí una función que reciba un número y devuelva True si es número primo, y False en caso contrario.
'''

def primos(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num%(i)==0:
                return False
        return True

print(primos(-1))
print(primos(0))
print(primos(1))
print(primos(2)) #False
print(primos(3))
print(primos(4)) #False
print(primos(5))
print(primos(6)) #False
print(primos(7))
print(primos(8)) #False