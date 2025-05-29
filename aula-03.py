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