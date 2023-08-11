
qtdsaque = 0;
saldo = 0;
i=0;
extrato = [];
usuarios_clientes = [];
contacorrente = [];

#classe "Conta-Corrente"
class ContaCorrente:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario

def criarContaCorrente():
    print("Criando uma Conta-Corrente:\n");

    if not usuarios_clientes:
       print("Erro: Nenhum usuário cadastrado para vincular a conta corrente.")
       return None;
    
    # A agência é fixa como "0001"
    agencia = "0001"
    
    # Se já existem contas, o número da próxima conta será o último número + 1
    if contacorrente:
        ultimo_numero_conta = contacorrente[-1].numero_conta
        numero_conta = ultimo_numero_conta + 1
    else:
        # Caso não existam contas, inicia com o número 1
        numero_conta = 1
    
     # Selecionar um usuário existente para vincular à nova conta corrente
    print("Usuários/Clientes disponíveis:")
    for indiceCliente, cliente in enumerate(usuarios_clientes):
        print(f"{indiceCliente + 1}. Nome:", cliente["nome"])
    selecao = int(input("Digite o número do usuário/cliente para vincular à conta: "))
    if 1 <= selecao <= len(usuarios_clientes):
        usuario_selecionado = usuarios_clientes[selecao - 1]
    else:
        print("Seleção inválida.")
        return
    
    # Criar a nova conta corrente e adicioná-la à lista
    nova_conta = ContaCorrente(agencia, numero_conta, usuario_selecionado)
    contacorrente.append(nova_conta)
    
    print("Conta corrente criada e vinculada ao usuário:")
    print("Agência:", nova_conta.agencia)
    print("Número da Conta:", nova_conta.numero_conta)
    print("Usuário vinculado:", usuario_selecionado["nome"])
    print("---------------------------")


def criarUsuario():
    print("Criando um Usuário/Cliente:\n");

    nome = str(input("Digite o Nome do Cliente:"));
    data_nascimento = str(input("Digite a Data de Nascimento:"));
    cpf =  str(input("Digite o CPF do Cliente:"));
    endereco = str(input("Digite o Endereço do Cliente:"));

    for cliente in usuarios_clientes:
        if(cliente["cpf"]==cpf):
            print("Error: Cpf já cadastrado.");
            return None;
        
    #adicionando os dados do novo cliente/usuário:
    novo_cliente = {
        "nome":nome,
        "dataNascimento":data_nascimento,
        "cpf":cpf,
        "endereço":endereco
    }
    #adicionando usuarios/clientes a lista:
    usuarios_clientes.append(novo_cliente);
    print("Usuário Cadastrado !!!");


def consultarExtrato():
    print("Consulta - Extrato");
    print(extrato);

def realizarDeposito():
    global saldo;

    print("Depósito");
    deposito = float(input("Informe o Valor do Depósito R$:"));
    #aqui está adicionando o depósito no extrato:
    extrato.append(('Depósito', deposito));
    saldo = deposito + saldo;
    print("Saldo Atualizado:\t R$", saldo);

def realizarSaque():
    global saldo;
    global saque;
    global qtdsaque;
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


def consultaSaldo():
    print("consulta do saldo:\t R$", saldo);
 

def informarSaldo():
  print("Informar o Saldo:");
  global saldo;
  saldo = float(input("Informe o valor do saldo R$:"));
  return saldo;

print("\n################ BEM VINDO AO BANCO #################");
print("Só é permitido realizar 3 Saques de 500,00 reais cada");
print("#####################################################");

while (qtdsaque < 3):

    print("\n################ BEM VINDO AO BANCO #################");
    print("[1] - para Informar o Saldo poupança");
    print("[2] - para consultar Saldo poupança");
    print("[3] - para Informar o Valor do Saque da conta-poupança");
    print("[4] - para Depositar na conta poupança");
    print("[5] - para Ver o Extrato");
    print("[6] - para adicionar cliente/usuário");
    print("[7] - para ver a lista de clientes/usuários");
    print("[8] - para adicionar conta-corrente");
    print("[9] - para ver a lista de conta-corrente");
    print("[10] - para sair");
    print("Só é permitido realizar 3 Saques de 500,00 reais cada");
    print("#####################################################\n");

    opcao = int(input("Informe a Opção:"));
    
    #Informar o Saldo:
    if opcao == 1:
        #chamando a função informarSaldo:
        informarSaldo();
    
    #Consultar o Saldo:
    elif opcao == 2:
        #chamando a função consultarSaldo:
        consultaSaldo();
    
    #Saque:
    elif opcao == 3:
        #chamando a função realizarSaque:
        realizarSaque();
    #Depósito:
    elif opcao == 4:
        #chamando a função realizarDeposito:
        realizarDeposito();
    #Extrato:
    elif opcao == 5:
        #chamando a função consultarExtrato:
        consultarExtrato();
    
    #Cliente/Usuário:
    elif opcao == 6:
        criarUsuario();
        
    
    #lista - clientes/usuários:
    elif opcao == 7:
        print("\n----------------------------------------------\n");
        print("Lista de Usuários Cadastrados:");
        print("Lista de Usuários/Clientes:");
        for cliente in usuarios_clientes:
            print("Nome:", cliente["nome"]);
            print("Data de Nascimento:", cliente["dataNascimento"])
            print("CPF:", cliente["cpf"]);
            print("Endereço:", cliente["endereço"]);
            print("----------------------------------------------");
    
    #Conta-Corrente:
    elif opcao == 8:
        criarContaCorrente();
    #listas - conta-corrente:
    elif opcao == 9():
        print("\n----------------------------------------------\n");
        print("Listas de Contas-Correntes já Cadastradas\n");

        for conta in contacorrente:
            print("Agência:", conta.agencia);
            print("Número da Conta:", conta.numero_conta);
            print("---------------------------");
    #Sair do Programa:
    elif opcao == 10:
        print("##### Você Saiu do Programa #####");
        break;


