# 7. Determinar el factorial de un número n, donde: n! = n·(n−1)·(n−2)..,3·2·1
n = int(input("Ingrese un numero: "))
r = 1 #Se guardara el resultado aqui, se usa el uno para que al multiplicarlo no cambie el resultado
c = 1 #Contador 

while c <= n: #Se establece que 4 es el numero al que se debe sacar el factorial
    r = r * c                                                                 #Ejemplo de factorial: 4
    c += 1   #Se cuenta de uno en uno hasta llegar a 4                        #1 * 2 * 3 * 4 = 24
                                                                           
print(f"Su factorial es: {r}")                                             
                                                                           