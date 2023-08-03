print("exemplo1: Estruturas de Repetição - utilizando iteravel: \n");
texto = str(input("Informe um Texto: "));
#aqui estou informando quais são as vogais:
VOGAIS = "AEIOU"

#aqui ele está perguntando se esta letra está contida nesse texto digitado

for letra in texto:
    #upper(): ele pega letra por letra minuscula e transforma em maiúscula:   
    # no 1 if é letras da palavra digitada que é vogal: 
    if letra.upper() in VOGAIS:
        print("\nVOGAL:", letra, end="")
    # no 2 if é letras da palavra digitada que não é vogal: 
    elif letra.upper() not in VOGAIS:
        print("\nNão VOGAL:", letra)       
else:
    print();

print("exemplo2: Estruturas de Repetição - Utilizando o Range com o for: \n");
#aqui consigo fazer ele gerar do numero inicial = 7 até o numero final = 21 - 1 
# dando de 7 até 20:  
for numero  in range(7, 21):
    print(numero, end=" ");

print("\nexemplo3: Estruturas de Repetição - Utilizando o While: \n");

print("\n***********MENU**************\n");
print("GOL G5/Palio/Clio/Celta/GOL G6/");
print("\n***********MENU**************\n");

modelo_veiculo = '1';

while modelo_veiculo != 'SAIR':
    modelo_veiculo = str(input("Informe o Nome do Veiculo:"));

    if modelo_veiculo == 'GOLG5' or modelo_veiculo == 'GOLG6':
        print("Você escolheu um carro da marca volkswagen, parabéns pela escolha");
    elif modelo_veiculo == 'Palio':
        print("Você escolheu um carro da marca Fiat, parabéns pela escolha");
    elif modelo_veiculo == 'Clio':
        print("Você escolheu um carro da marca Renault, parabéns pela escolha");
    elif modelo_veiculo == 'Celta':
        print("Você escolheu um carro da marca chevrolet, parabéns pela escolha");
    elif modelo_veiculo == 'SAIR':
        print("Voce Saiu de Nosso Sistema");
    else:
        print("*** ERROR, Digite e escolha somente os carros válidos no menu ***");

print("\nexemplo4: Estruturas de Repetição - Utilizando o While e break: \n");

print("\n***********MENU**************\n");
print("Idade for maior ou igual À 18 anos = MAIOR DE IDADE");
print("Idade for menor que 18 anos = MENOR DE IDADE");
print("\n***********MENU**************\n");

idade = -10;

while idade != -1:

    idade = int(input("Informe a Idade: "));

    if idade >= 18:
        print("maior de idade");
    elif idade < 18:
        print("menor de idade");
        #o break corta o programa direto:
        break;



    







