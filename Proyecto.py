# importar la clase para leer
from lector_excel import Lector
import os
 
# funcion con parametro de entrada
def leer_archivo(nombre_archivo, col):
    # crear un objeto para leer a partir de la clase
    archivo_excel = Lector(nombre_archivo)

    # leer columna
    columna = archivo_excel.leer_columna(col)
 
    # eliminar primer elemento porque es un string
    columna.pop(0)
    
    # sumar los valores de la columna
    valsColumna = [celda for celda in columna]

    return valsColumna
 
carpeta_entrada = "final"
# listar todos los archivos de una carpeta
lista_archivos = os.listdir(carpeta_entrada)
print(lista_archivos)

sumas_total_v = []
sumas_total_c = []
sumas_total_g = []

promedios_c = 0
promedios_g = 0
mes=0
# recorriendo la lista de archivos
for nombre_archivo in lista_archivos:
    
    venta = leer_archivo((f'final//{nombre_archivo}'), 'B')
    costo = leer_archivo((f'final//{nombre_archivo}'), 'C')
    ganancia = leer_archivo((f'final//{nombre_archivo}'), 'D')
    
    promedio_costo = round(sum(costo) / len(costo),1)
    promedio_ganancia = round(sum(ganancia) / len(ganancia),1)
    
    promedios_c += promedio_costo
    promedios_g += promedio_ganancia
    #Mes = Mes + 1
    mes+=1

    for v in venta:
        sumas_total_v.append(v)

    for c in costo:
        sumas_total_c.append(c)

    for g in ganancia:
        sumas_total_g.append(g)
    
    print()
    nombre_mes = nombre_archivo[3:-5]
    print("=== MES", nombre_mes.upper(), " ===")
    
    print("Total de costo: \t", sum(costo))
    print("Promedio de costo: \t", promedio_costo)
    print("Total de Ganancia: \t", sum(ganancia))
    print("Promedio de Ganancia: \t ", promedio_ganancia)
    
    print()
print("====================")

print("Suma total de costos: ", sum(sumas_total_c))
print("promedio total de costo: ", promedios_c / mes )

print("Suma total de Ganacia: ", sum(sumas_total_g))
print("promedio total de ganancia: ", promedios_g / mes )

print()
print("====================")
print("MES con venta más alta: ",max(sumas_total_v))
print("MES con costo más alto: ",max(sumas_total_c))
print("MES con ganancia más baja: ",min(sumas_total_g))

