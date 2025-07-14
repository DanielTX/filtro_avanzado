from src.filtro import procesar_numeros

numeros = [1, 2, 3, 4, 5, 6]
resultado = procesar_numeros(numeros)

print("Pares:", resultado['pares'], "Suma:", resultado['suma_pares'])
print("Impares:", resultado['impares'], "Suma:", resultado['suma_impares'])
