c, p, f = input().split()
c = int(c)
p = int(p)
f = int(f)


if (1<=c<=1000) and (1<=p<=1000) and (1<=f<=1000):

    if f*c<=p:
        print("s")

    else:
        print("n")

else:
    print("Há algum valor inválido nas informações que você digiou. Digite valores entre 1 e 1000")



