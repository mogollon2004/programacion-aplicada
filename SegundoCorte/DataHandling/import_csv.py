import random
import csv

# Generar una lista de números aleatorios entre 0 y 1
numeros = [random.uniform(0, 1) for _ in range(30)]  # Generamos 30 números aleatorios

# Filtrar los números mayores a 0 y menores a 1
numeros_filtrados = [num for num in numeros if 0 < num < 1]

# Especifica el nombre del archivo CSV en el que deseas guardar los números
nombre_archivo = "numeros.csv"

# Guardar los números filtrados en el archivo CSV con un máximo de 10 números por fila
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(["Numero"])  # Escribir el encabezado

    fila_actual = []
    for num in numeros_filtrados:
        fila_actual.append(num)
        if len(fila_actual) == 10:
            escritor_csv.writerow(fila_actual)
            fila_actual = []

    # Asegurarse de que los números restantes se escriban en la última fila
    if fila_actual:
        escritor_csv.writerow(fila_actual)

print(f"Los números filtrados se han guardado en '{nombre_archivo}'.")
