# 2. Construir un programa que calcule e imprima la sumatoria: 

# S =500+456+510+454+520+452+...+800  
n = 0 #Se empieza con el cero, se usara para el while
n1 = 500 #Primer numero               #El patron de la sumatoria indica que el primer numero y el segundo tienen diferentes patrones, el primero avanza en 10 despues del segundo y el segundo 
n2 = 456 #Segundo numero              #retrocede 2 despues del tercero y asi susesivamente. Se crean 2 variables      

while n1 <= 800 and n2 <= 800: #Se establece 800 como limite
    n += n1     #Se aplica al n que empieza de 0
    n += n2     
    n1 += 10    #Se aplica el patron  
    n2 -= 2 
print(f"La suma es de {n}")
