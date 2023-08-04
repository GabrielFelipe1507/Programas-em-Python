#exemplo de conjunto abaixo:
print("tipo sets:");

carro = {"golg5", "golg5", "celta"};
#repare que ele remove os valores duplicados e repare também que ele
#mostra sem inportar a ordem que estava esses valores:
print(carro);

# se for um set vc precisa converter ele pra lista para dái acessá-lo:
carros = {"corsa", "space-fox", "vectra"};
#aqui abaixo no print dará erro pois ainda não foi convertido para lista:
#print(carro[0]);
#aqui já está convertendo do tipo set para lista:
carros = list(carros);
#agora consigo acessar:
print(carros[0]);

print("\ntipo union:");
print("\nconjuntoa = {a, b}\nconjuntob = {c, d}\n");
conjuntoa = {"a", "b"}
conjuntob = {"c", "d"}

#aqui passo qual conjunto se une com qual:
print(conjuntoa.union(conjuntob));

print("tipo intersection:");
conjuntoa = {"a", "b", "c"}
conjuntob = {"a", "b", "d"}

#na intersecção é tudo que está no conjunto "a" eu ter no conjunto "b":
print(conjuntoa.intersection(conjuntob));

#já aqui é o que tem de diferente entre um conjunto e outro:
print("tipo diference:");
print("conjuntoa.difference(conjuntob):", conjuntoa.difference(conjuntob));
print("conjuntob.difference(conjuntoa):", conjuntob.difference(conjuntoa));

#tipo add:
print("tipo add:");
numeros = {1, 2, 3}
print(numeros);
#aqui ele adiciona um numero:
numeros.add(4);
print(numeros);

#tipo discard:
#aqui ele discarta um valor ou tira um valor da lista:
numeros.discard(2);
print(numeros);

#tipo remove:
#é igualzinho do discard a unica diferença é que ele dá erro quando pede pra 
#remover um elemento do conjunto que não existe já o discard nao dá erro ele
#simmplesmente não remove:

#numeros.remove(5);

#tipo len:
print("Tipo Len:\nMostra o Tamanho do Conjunto:", len(numeros));

#se eu quiser saber se um elemento está no conjunto é só eu utilizar o "In":
print(5 in numeros); #False
print(1 in numeros); #True


