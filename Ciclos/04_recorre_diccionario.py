#Diccionario: Es un tipo de colección compuesta por varios elementos que
#             poseen Clave-Valor

numeros_telefonicos = {"Contacto 1":2721238756,"Contacto 2":2729871276,"Contacto 3":2725463298}

#items() permite acceder a los valores del diccionario

for clave,valor in numeros_telefonicos.items():
    print("Clave:", clave, "Valor:", valor)
    #print("Clave: " + clave + " valor: " + str(valor))