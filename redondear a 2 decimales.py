'''
Escribí un código que resuelva las siguientes preguntas:
1. Si tengo 15 huevos, ¿cuántos maples de 6 unidades puedo completar?
2. Una bolsa con 14 canicas pesa 234gr. Con una exactitud de dos decimales, ¿cuánto pesan 5 canicas?

Para redondear a dos decimales: round(valor,cant_decimales).
'''

#Ejercicio 1
huevos = 15
huevos_por_maple = 6 

maples_completos = huevos // huevos_por_maple

print(maples_completos)

#Ejercicio 2
peso_bolsa_canicas = 234.0
canicas_por_bolsa = 14.0

peso_canica =  peso_bolsa_canicas/canicas_por_bolsa

peso_cinco_canicas =  round(5*peso_canica,2)
print(peso_cinco_canicas)
