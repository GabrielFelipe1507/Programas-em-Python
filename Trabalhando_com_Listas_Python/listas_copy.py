#lista em python:
lista = [1, "Python", [40,30,20]]

#o copy faz uma cópia da lista original para que quando vc altere um valor na lista nao 
# seja alterado este valor na lista original.
#lista copiada(l2):
l2 = lista.copy();
#lista original sendo printada:
print(lista);
#aqui abaixo se vc for printar os "id's" das listas(original e cópia) vc percebe q as listas
# estão em locais diferentes na memória:
print(id(l2), id(lista));

#aqui vou dar um exemplo de alteração de valores sem interferência na lista original:
l2[0]= 100;

print("Lista sem alteração:");
print(lista);
print("Lista Copiada com Alteração:");
print(l2);
