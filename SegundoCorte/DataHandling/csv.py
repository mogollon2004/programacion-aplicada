import random
import csv

# Generar una lista de números aleatorios entre 0 y 1
numeros = [random.uniform(0, 1) for _ in range(10)]  # Puedes ajustar la cantidad de números que deseas generar

numeros_filtrados = [num for num in numeros if 0 < num < 1]

nombre_archivo = "numeros.csv"

with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Numero"])  # Escribir el encabezado
    escritor_csv.writerows([[num] for num in numeros_filtrados])

print(f"Los números filtrados se han guardado en '{nombre_archivo}'.")
