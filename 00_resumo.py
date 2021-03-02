lista_um = [1, 2, 3]
print(lista_um)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

x = 123
lista_um.append(x) # Armazena o valor inserido na variável à lista desejada
print(lista_um)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

lista_um.insert(0, 321) # Zero (0) é o índice, 321 é o valor onde será inserido
print(lista_um)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

lista_um.remove(1) # O 1 é o valor equivalente da lista, ele será removido
print(lista_um)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

lista_um.pop(3) # O 3 é a posição/índice do valor que será removido
print(lista_um)   # Neste caso, foi removido o valor '123'
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

lista_um.clear() #esvazia a lista
print(lista_um)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')


print()
lista_dois = [321, 654, 876, 98, 123, 345, 567, 789, 890, 100]
print(lista_dois)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_dois.index(654)) # '654' é o valor que a lista possui, o resultado '1' é a sua posição/índice
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')


print()
lista_tres = [1, 1, 1, 3, 4, 5, 6, 10, 10]
print(lista_tres)
print(lista_tres.count(1)) # conta quantos '1' a lista possui
print(lista_tres.count(10)) # conta quantos '10' a lista possui
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_dois)
lista_dois.sort() # Ordena a lista desejada em ordem crescente
print(lista_dois)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_dois)
lista_dois.reverse() # Ordena a lista desejada em ordem decrescente
print(lista_dois)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

lista_quatro = [55, 12, 134, 563, 97, 10]
copia = lista_quatro.copy() # Copia exatamente todos os valores da lista em seus respectivos índices
print(copia)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_quatro)
lista_quatro.extend([6, 7, 8]) # Adiciona os valores informados ao final da lista desejada
print(lista_quatro)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(len(lista_quatro)) # Mostra a quantidade de índices que a lista 4 possui, neste caso, 9, após a alteração acima
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(max(lista_quatro)) # Mostra o maior valor entre os índices da lista desejada, neste caso, 563
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(min(lista_quatro)) # Mostra o menor valor entre os índices da lista desejada, neste casom 6
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_quatro)
s = sorted(lista_quatro) # Mostra a lista em ordem crescente, assim como o "lista_quatro.sort()"
print(s)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_quatro)
print(sum(lista_quatro)) # Mostra a soma dos valores dos índices da lista desejada
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(lista_dois)
print(tuple(lista_dois)) # Mostra os elementos da lista desejada em forma de tupla "()" ao invés de "[]"
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
