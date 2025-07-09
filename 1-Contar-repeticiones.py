# 1. Contar las repeticiones de una palabra en una tupla:

# a) Lea el parrafo. Este debe ser ingresado por teclado.
p = input("Ingrese el parrafo: ") #Parrafo ingresado por teclado 

# b) Separe sus palabras y debe guardarlas en una lista.
ps = p.split() #Parrafo separado    
pl = list(ps) #Lista
 
# c) Solicite al usuario una palabra a buscar.
pb = input("Ingrese una palabra a buscar en el parrafo: ") #Palabra a buscar

# d) Imprima cuántas veces aparece dicha palabra (Debe ser sensible a mayúsculas y minúsculas).
pc =  pl.count(pb) #Palabras a contar 
print(f"La palabra {pb} se encuentra {pc} veces en el parrafo.")

# Requisito especial: Si el párrafo está vacio. debe lanzar y capturar una excepción (ValueError) indicando “El texto no puede estar vacío”.   
cc = len(p) #Contador de caracteres (Los espacios se cuentan)
if cc <= 0:
    raise ValueError("El texto no puede estar vacio.") 
else: 
    print("El codigo es sensible a mayusculas y minusculas, por lo que una diferencia menor puede afectar la cuenta.") #Recordatorio como relleno de texto