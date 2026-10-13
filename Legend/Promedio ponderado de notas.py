# Promedio ponderado de notas
# Este programa calcula el promedio ponderado de un conjunto de notas.
# Autor: Daniel Alejando Vera Mendoza
# Fecha: 2026-10-12
# Función para determinar el promedio ponderado de un conjunto de notas

import decimal


def promedio_ponderado(valor_notas, valor_pesos):
    total = len(valor_notas)
    x = 0
    suma = decimal.Decimal(0)
    suma_pesos = decimal.Decimal(0)

    while x < total:
        y = valor_notas[x] * valor_pesos[x]
        suma = suma + y
        suma_pesos = suma_pesos + valor_pesos[x]
        x = x + 1

    if suma_pesos == 0:
        print("Error: la suma de los pesos no puede ser cero")
        return

    promedio = suma / suma_pesos

    print("El promedio ponderado es:", promedio)

    if promedio < 3:
        print("No aprobado")
    else:
        print("Aprobado")


# Ingreso de datos
notas = []
pesos = []

n = int(input("Ingrese el número de notas: "))

for i in range(n):
    nota = decimal.Decimal(
    input("Ingrese el valor de la nota: ").replace(",", ".")
    ) 

    peso = decimal.Decimal(
    input("Ingrese el valor del peso: ").replace(",", ".")
    )

    notas.append(nota)
    pesos.append(peso)

promedio_ponderado(notas, pesos)
