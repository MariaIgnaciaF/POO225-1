#entrada de datos
laVariable = input("Introduce un valor: ")
#salida de datos
print("El valor introducido es: ", laVariable)
#Entrada - Proceso - Salida
edad = input("Introduce tu edad: ")
#proceso de datos
edad = edad*2
print("Tu edad es: ", edad)

#Decisión IF
if(edad<18):
    print("Eres menor de edad")
    print("No puedes entrar")
else:
    print("Eres mayor de edad")
    print("Puedes entrar")
    if(edad>65):
        print("Eres jubilado")
        print("Puedes entrar gratis")
#Ciclos
i=0
while(i<10):
    print(i)
    i=i+1
#Ciclo for
for i in range(10):
    print(i)
milista=[1,2,3,4,5,6,7,8,9,10]
for i in milista:
    print(i)
    