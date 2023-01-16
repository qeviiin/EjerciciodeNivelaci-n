import random
random.randint(0,10)
random=random.randint(0,10)
print("Tu número aleatorio es ", random)
numero=int(input("Ingresa un número "))
while random:
    if numero>random:
        print("El valor debe ser más pequeño")
        numero=int(input("Ingresa un número "))
    
    if numero==random:
        print("BINGO")
        break
    if numero<random:
        print("El valor debe ser más grande")
        numero=int(input("Ingresa un número "))
