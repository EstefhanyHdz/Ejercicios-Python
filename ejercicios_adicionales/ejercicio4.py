#Algoritmo, que calcule el tiempo de encuentro 
#de 2 vehículos que van en sentido opuesto, 
#teniendo como datos la distancia inicial que 
#los separa y la velocidad de cada uno.

print("Ingresa las velocidades de los dos vehículos:")
velocidad1 = float(input("Velocidad del vehículo 1: "))
velocidad2 = float(input("Velocidad del vehículo 2: "))
print("Ingresa la distancia inicial que los separa:")
distancia = float(input("Distancia: "))

if velocidad1 > 0 and velocidad2 > 0:
    tiempo = distancia / (velocidad1 + velocidad2)
    print("El tiempo de encuentro es en: ")
    print(tiempo)
else:
    print("ERROR")