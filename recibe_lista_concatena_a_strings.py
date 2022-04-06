'''
Escribí una función que reciba una lista y concatene 
los elementos de la lista en un único string.
'''

def concat_string(x):
  cadena = "".join(x)
  return cadena
    

milista = ["1","a","4","d","e","o","s"]
var = concat_string(milista)
print(var)