c=int(input("Número de competidores: "))
p=int(input("Número de folhas de papel especial: "))
f=int(input("Número de folhas que cada competidor irá receber: "))

if f*c<=p:
    print("s")

elif (1<=c<=1000) or (1<=p<=1000) or (1<=f<=1000):
    print("Há algum valor inválido nas informações que você digiou. Digite valores entre 1 e 1000")
    
else:
    print("n")
