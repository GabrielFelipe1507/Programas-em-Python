
qtdsaque = 0;
saldo = 0;
i=0;
extrato = [];

print("################ BEM VINDO AO BANCO #################");
print("Só é permitido realizar 3 Saques de 500,00 reais cada");
print("#####################################################");

while (qtdsaque < 3):

    print("################ BEM VINDO AO BANCO #################");
    print("[1] - para Informar o Saldo");
    print("[2] - para consultar Saldo");
    print("[3] - para Informar o Valor do Saque");
    print("[4] - para Depositar");
    print("[5] - para Ver o Extrato");
    print("[6] - para sair");
    print("Só é permitido realizar 3 Saques de 500,00 reais cada");
    print("#####################################################");

    opcao = int(input("Informe a Opção:"));
  
    #Informar o Saldo:
    if opcao == 1:
        print("Informar o Saldo:");
        saldo = float(input("Informe o valor do saldo R$:"));
    #Consultar o Saldo:
    elif opcao == 2:
        print("consulta do saldo:\t R$", saldo);
    #Saque:
    elif opcao == 3:
        print("Informar o valor do Saque:");
        saque = float(input("Informe o valor do Saque R$:"));

        if (saque>0 and saque<=500 and saque <= saldo):
            
            extrato.append(('Saque', saque));
            qtdsaque += 1;
            saldo = saldo - saque;
            print("Saldo Atualizado:\t R$", saldo);
             
        elif (saque>saldo):
            print("Não Será possivel sacar o dinheiro por falta de Saldo R$");
        elif(saque>500):
            print("Só é permitido realizar Saques até R$ 500,00 reais");
    #Depósito:
    elif opcao == 4:

        print("Depósito");
        deposito = float(input("Informe o Valor do Depósito R$:"));
        extrato.append(('Depósito', deposito));
        saldo = deposito + saldo;
        print("Saldo Atualizado:\t R$", saldo);
    
    elif opcao == 5:
        print("Consulta - Extrato");  

        print(extrato);
    #Sair do Programa:
    elif opcao == 6:
        print("##### Você Saiu do Programa #####");
        break;


