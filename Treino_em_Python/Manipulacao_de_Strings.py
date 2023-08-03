nome = "GaBrIel";

print("upper, lower, title:\n");
# 'upper()' toda letra maiuscula:
print(nome.upper())
# 'lower()' toda letra minuscula:
print(nome.lower())
# 'title' somente o primeiro carcter da string em maiusculo:
print(nome.title())

texto = "  Olá Mundo!   ";

print("strip, lstrip, rstrip:\n");

#print comum:
print(texto);
# remove os espaços da string:
print(texto.strip() + ".");
# remove o espaço da esquerda da string:
print(texto.lstrip() + ".");
# remove o espaço da direita da string:
print(texto.rstrip() + ".");

print("Centralização:\n")
#Centralização: util pra criação de menus que centralizem bunito e organizado a string:

menu = "Python";
print("####" + menu + "####");
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n");

for letra in menu:
    print(letra, end="-");
print();

print("-".join(menu));

print("Fatiamento de String:\n");
#Fatiamento de String:

nome = "Gabriel Felipe da Silva"

#aqui retorna somente a letra da posição 0 da String:
print(nome[0]);
#aqui pega até da posição 7 da string da variavel nome:
print(nome[:7]);
#aqui pega apartir da posição 8 da string da variavel digitada:
print(nome[8:]);
#aqui ele pega o inicio e o fim passados no colchetes:
print(nome[8:18]);
#aqui ele pega as letras de 2 em dois mais posso aumentar pra 3 em tres ou mais sucessivamente:
print(nome[0:23:2]);
#ele retorna aqui somente a string inteira:
print(nome[:]);
#aqui ele vai criar uma cópia da string só que invertida:
print(nome[::-1]);
#aqui ele pega ultima letra da string:
print(nome[-1]);

print("\nConcatenação de Strings:\n");
#concatenação de strings:
nome = "Gabriel Felipe da Silva";
idade = 26
faculdade = "BCC - Bacharelado em Ciências da Computação"
instituição = "IFSP"

#aqui faço a concatenação das strings:
mensagem = f''' Meu Nome é {nome}, tenho {idade} anos e gosto de Futebol, além disso
faço Faculdade de {faculdade} no {instituição}''';

print(mensagem);

