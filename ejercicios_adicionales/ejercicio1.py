#Dado el sueldo de un trabajador, aplique un aumento del 15% si su sueldo es inferior a $1000. 
#Imprima el sueldo que percibirá.
sueldo = float(input("Ingresa tu sueldo: "))
aumento = float (sueldo * 0.15)
sueldo_final = float (sueldo + aumento)
if sueldo < 1000:
    print("\nTu sueldo con aumento es: ")
    print(sueldo_final)