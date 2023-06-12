n1 = 37
n2 = 11
r = n1%n2
cont = 0

while r!=0:
    cont += 1
    n1=n2
    n2=r
    r=n1%n2
    print(r)

print(cont)