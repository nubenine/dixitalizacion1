numeros = input("Dime una lista de numeros, separalos por espacios")
list = [int(n) for n in numeros.split()]
pares = []
impares = []

for element in list:
    if element % 2 != 0:
    	impares.append(element)
    else: 
        pares.append(element)
       
                
    
    
print("Números pares: ", pares)
print("Números impares: ", impares)		
