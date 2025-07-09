#Letra A#

quellondict = {"Ciudad":"Quellón","Temperatura":10.2,"Precipitacion":2950}
chonchidict = {"Ciudad":"Chonchi","Temperatura":8.3,"Precipitacion":2800}
castrodict = {"Ciudad":"Castro","Temperatura":11.8,"Precipitacion":2000}
superdict = {5700000: castrodict, 5770000: chonchidict, 5790000:quellondict}
print(superdict)
print()

#Letra B#

def climate(float):
    try:
        if float < 10:
            return "Frío"
        elif float>=10 and float<=15:
            return "Templado"
        elif float>15:
            return "Cálido"
    except:
        return "Desconocido"

superdict[5790000]["Clima"]= [climate(superdict[5790000]["Temperatura"])]
superdict[5770000]["Clima"]= [climate(superdict[5770000]["Temperatura"])]
superdict[5700000]["Clima"]= [climate(superdict[5700000]["Temperatura"])]
print(superdict)
print()

#Letra C#

superdict[5700000]["Meses más lluviosos"]=[]
superdict[5700000]["Meses más lluviosos"].append("mayo")
superdict[5700000]["Meses más lluviosos"].append("junio")
superdict[5700000]["Meses más lluviosos"].append("julio")
superdict[5700000]["Meses más lluviosos"].remove("junio")
print(superdict)
print()

#Letra D#

superdict[5770000]["Ciudad"]="Ciudad de los Tres Pisos"
print(superdict)
print()

#Letra E#

Precipitaciones=[superdict[5770000]["Precipitacion"],superdict[5700000]["Precipitacion"],superdict[5790000]["Precipitacion"]]

print("suma precipitaciones: ", sum(Precipitaciones))
print("precipitación máxima y mínima: ", max(Precipitaciones), min(Precipitaciones))
print("posición precipitación máxima: ", Precipitaciones.index(max(Precipitaciones)))
print()

#Letra F#

print(superdict)
print()

#Letra G#

superlist=[superdict.items()]
print(superlist)

