#ordenar una lista respecto otra
t = ["a","b","c","d","e","f"]
n = [1,23,4,5,67,9]

Z = [t for _,t in sorted(zip(n,t))]
X = sorted(n)
print("Dptos Orden",X)
print("Antenas: ",Z)