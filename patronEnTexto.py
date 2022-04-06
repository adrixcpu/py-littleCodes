import re
 
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
patron = "Lorem"
 
x = re.search(patron, texto) #Busca el patron dentro del texto
 
print(x.span()) #Escribe la posicion inicial y final de la ocurrencia

tipoAntena = input("Ingrese el tipo de nuevas antenas: ")

x = re.search("[a-e]", tipoAntena)
y = re.search("[abcde]", tipoAntena)

if x:
  print("YES! We have a match!")
  print(tipoAntena)
else:
  print("No match")
  print(tipoAntena)

  
if y:
  print("YES!!")
  print(tipoAntena)
else:
  print("Nooo")
  print(tipoAntena)