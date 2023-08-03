print("exemplo1: Indentação e blocos:");

saldo = 500;

def retirar(valor):
    if(saldo>=valor):
        print("valor sacado");
        print("retire o seu dinheiro na boca do caixa");
    
    print("Obrigado por ser nosso cliente !!!");

def depositar(valor):
    saldo = 500
    saldo == valor;

retirar(100);
depositar(1000);

print("exemplo2: Estruturas condicionais:");
opcao  = int(input("\nInforme uma opção: [1] Sacar : [2] Extrato: \t"));

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "));
#ao invés de elseif igual em linguagem C utiliza-se elif se tiver mais de duas condições
# e só por ultimo que utiliza-se o else:
elif opcao == 2:
    print("Exibindo o Extrato");
else:
    print("Inválido !!!");

#Outro exemplo de else e if:
print("\n***********MENU**************\n");
print("GOL G5/Palio/Clio/Celta/GOL G6/");
print("\n***********MENU**************\n");
modelo_carro = str(input("Informe o Moldelo do Carro que deseja compra:"));

if modelo_carro == 'GOLG5' or modelo_carro == 'GOLG6':
    print("Você escolheu um carro da marca volkswagen, parabéns pela escolha");

elif modelo_carro == 'Palio':
    print("Você escolheu um carro da marca Fiat, parabéns pela escolha");
elif modelo_carro == 'Clio':
    print("Você escolheu um carro da marca Renault, parabéns pela escolha");
elif modelo_carro == 'Celta':
    print("Você escolheu um carro da marca chevrolet, parabéns pela escolha");
else:
    print("*** ERROR, Digite e escolha somente os carros válidos no menu ***");

