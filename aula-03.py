## Listas
#1. Crie uma lista com as strings `'infinity'`, `'school'`, `'curso'`, `'dfs'`.
lista = ['infinity','school','curso','dfs']

#2. Insira a string `'python'` na lista do exercício acima.
lista.append('python')

#3. Imprima a lista após remover o primeiro elemento dela.
lista.pop(0)
print(lista)

#4. Imprima a lista após remover o último elemento dela.
lista.pop()
print(lista)

#5. Defina que o terceiro elemento da lista será `'course'` e imprima a lista.
lista[2] = 'course'
print(lista)

#6. Com a lista `['Mike', '', 'Emma', 'Kelly', '', 'Brad']`, imprima a lista sem as strings vazias.
lista = ['Mike','','Emma','Kelly','','Brad']

while '' in lista:
    lista.remove('')
print(lista)


## Tuplas
#1. Crie uma tupla com os números de 1 a 5.
numeros = (1,2,3,4,5)

#2. Imprima o segundo elemento da tupla.
print(numeros[1])

#3. Imprima o tamanho da tupla.
print(len(numeros))

#4. Concatene duas tuplas `(1, 2, 3)` `(4, 5, 6)`. Imprima a tupla concatenada.
tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = tupla1 + tupla2
print(tupla3)

#5. Crie uma tupla `(5, 10, 15)`, converta a tupla para lista, adicione o número `40` e imprima a tupla resultante.
tupla = (5,10,15)
lista = list(tupla)

lista.append(40)
tupla = tuple(lista)
print(tupla)
