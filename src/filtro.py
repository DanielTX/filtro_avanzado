def filtrar_pares_impares(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares

def sumar_lista(lista):
    return sum(lista)

def procesar_numeros(lista):
    pares, impares = filtrar_pares_impares(lista)
    suma_pares = sumar_lista(pares)
    suma_impares = sumar_lista(impares)
    return {
        'pares': pares,
        'suma_pares': suma_pares,
        'impares': impares,
        'suma_impares': suma_impares
    }
