#Construya un algoritmo que, dados tres números, 
# muestre el mensaje “IGUALES” si la suma de los 
# dos primeros es igual al otro número y el 
# mensaje “DISTINTOS” en caso contrario.
print("Ingresa tres números enteros: ")
primero = int(input("Primer número: "))
segundo = int(input("Segundo número: "))
tercero = int(input("Tercer número: "))

if primero + segundo == tercero:
    print("IGUALES")
else:
    print("DISTINTOS")