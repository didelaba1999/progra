# 3. Tres vendedores de una tienda de ropa deportiva registran sus ventas diarias durante 5 días. Los vendedores obtienen un bono por cierta cantidad de ventas realizadas durante la semana:

# Venta semanal total superior a $1.500.000 (Bono de un 20% del sueldo base) #20 = 0.20 
# Venta semanal total superior a $1.000.000 (Bono de un 10% del sueldo base) #10 = 0.10 
# Venta semanal total superior a $500.000 (Bono de un 5% del sueldo base)    #5 = 0.05 

# Además considerar: Sueldo Base en Chile 2025 es de $529.000
sb = 529000
# Se solicita:

# a) Crea un diccionario donde la clave sea el nombre del vendedor y el valor otra estructura que guarde las ventas diarias (Puede ser una lista o tupla)
vv = {
    "Primer vendedor" : (200000, 600000, 200000, 300000, 200000),
    "Segundo vendedor" : (200000, 200000, 200000, 200000, 200000),    #Al no especificarse los valores diarios se inventan para los 5 dias, se establecen para cada bono de tal forma que se
    "Tercer vendedor" : (100000, 100000, 100000, 100000, 100000)     #compruebe la funcionalidad del codigo
}

# b) Calcula el total de las ventas semanales de cada vendedor y su bono si le corresponde.
for v, vt in vv.items():  #Se recurre al items para sacar valores del diccionario, se establece v(vendedor) como clave y vt(ventas) como valor 
    tv = sum(vt) #Total de ventas
    if tv >= 1500000:
     b = sb * 0.20
    elif tv >= 1000000:
     b = sb * 0.10  #Se establecen los distintos bonos
    elif tv >= 500000:
      b = sb * 0.05 
    else:
     b = 0 #Si no se cumplen las condiciones el bono es de 0 


# c) Obtener el promedio de ventas semanales de cada vendedor.
    cd = len(vt) #Cantidad de dias 
    p = tv / cd #Promedio (Total de ventas dividido por cantidad de dias)                  #Se mantiene todo en el for para que al imprimir aparezcan los 3 vendedores


# d) Imprime un reporte con el total del sueldo a pagar por cada vendedor.
    st = sb + b
    print(st)

#Los nombres de los vendedores y los valores de las ventas deben estar instanciado en código (Hardcodeado).
    print(f"{v}:")
    print(f"Total de ventas semanales: {tv}")
    print(f"Bono: ${b}")
    print(f"Promedio diario: ${p}")
    print(f"Sueldo total a pagar: ${st}")
    print("-" * 10) #Separa los registros de los vendedores con lineas