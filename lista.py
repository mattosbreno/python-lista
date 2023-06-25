lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

# Maior elemento
maior_elemento = max(lista)
print("Maior elemento:", maior_elemento)

# Menor elemento
menor_elemento = min(lista)
print("Menor elemento:", menor_elemento)

# Números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print("Números pares:", numeros_pares)

# Primeiro elemento da lista
primeiro_elemento = lista[0]
ocorrencias_primeiro_elemento = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", ocorrencias_primeiro_elemento)

# Média dos elementos
media_elementos = sum(lista) / len(lista)
print("Média dos elementos:", media_elementos)

# Soma dos elementos de valor negativo
soma_negativos = sum(num for num in lista if num < 0)
print("Soma dos elementos negativos:", soma_negativos)
