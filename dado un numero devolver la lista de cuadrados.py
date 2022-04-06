'''
Una función que devuelva una lista con todos los cuadrados de los números entre 1 y 30 (incluidos).
'''

def cuadrados():
    lista=[]
    for i in range(30):
        num=i+1         
        num **= 2   #El que se multiplica por si mismo es num tantas veces diga el número del frente
        lista.append(num)
    return lista

print(cuadrados())