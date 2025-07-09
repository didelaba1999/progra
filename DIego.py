#letra A
dict={
    101:{"nombre":"Luna","peso":1.2,"edad":3,"tamaño":30},
    102:{"nombre":"Michi","peso":0.8,"edad":2,"tamaño":25},
    103:{"nombre":"Pepito","peso":2.5,"edad":5,"tamaño":35},
}
print(dict)
print()
#letra B
def checapeso(int):
    if int<1:
        return "bajo-peso"
    elif int<=4 and int>=1:
        return "normal"
    else:
        return "sobrepeso"
    
for index, subdict in enumerate(dict.items()):
        dict[subdict[0]]["clasificacion-peso"]=checapeso(dict[subdict[0]]["peso"])

print(dict)
print()
#letra C
def checaedad(int):
    try:
        if int<4:
            return "cachorro"
        elif int<=12 and int>=4:
            return "joven"
        else:
            return "adulto"
    except:
        return "Desconocida"    

for index, subdict in enumerate(dict.items()):
        dict[subdict[0]]["categoria-etaria"]=checaedad(dict[subdict[0]]["edad"])
print(dict)
print()
#letra D
ingresopeso=[]
for index, subdict in enumerate(dict.items()):
    tuplatemp=(subdict[0],dict[subdict[0]]["peso"])
    ingresopeso.append(tuplatemp)

for index, tuple in enumerate(ingresopeso):
     print(tuple[1])
#letra E
while True:
    starter=input("desea ingresar un nuevo gatito?(y/n)")
    if starter=="n":
        break
    elif starter=="y":
        print("ingrese sus datos: ")
        ingreso=input("nro de ingreso: ")
        dict[int(ingreso)]={}
        
        dict[int(ingreso)]["nombre"]=str(input("nombre: "))
        dict[int(ingreso)]["peso"]=float(input("peso: "))
        dict[int(ingreso)]["edad"]=int(input("edad: "))
        dict[int(ingreso)]["tamaño"]=int(input("tamaño:"))
        print(dict)
        print()
    else:
        print("responda con (y/n)")
#letra f
paciente=int(input("numero de ingreso del paciente: "))
dict[paciente]["tamaño"]=int(input("ingrese el nuevo tamaño: "))
print(dict[paciente]["tamaño"])
print()
#letra G
listapeso=[]

for index, tuple in enumerate(ingresopeso):
    listapeso.append(tuple[1])
print(listapeso)
print("promedio: ", sum(listapeso)/len(listapeso))
print("min y max: ", min(listapeso), max(listapeso))
print("michi")