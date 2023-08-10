#funções em python:
def exibir_mensagem():
    print("Olá Mundo!");

def exibir_mensagem2(nome):
    print("Seja Bem Vindo {nome}!");

def exibir_mensagem3(nome= "Anônimo"):
    print(f"Seja Bem Vindo {nome}!");

def carros(ano, modelo, marca, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}");

def somar (a, b):
    return a + b;

def subtrair (a, b):
    return a - b;

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b);
    print(f"O resultado da operação {a} + {b} = {resultado}");


#aqui abaixo estou chamando as funções:
exibir_mensagem();
#passando o nome por parametro:
exibir_mensagem2(nome = "Gabriel");
exibir_mensagem3();
exibir_mensagem3(nome="Gabriel");

#chamando a função carros:
carros(2009, "GOl G5", "volkswagen", "POLU-9098");

#aqui ele printa e tras o resultado da soma da função "soma":
print(somar(3, 2));

#aqui embaixo tou usando a mesma função que pode chamar funções diferentes por parametros:
#aqui ele passa os valores a serem somados e a função "soma" que somará esses valores:
exibir_resultado(10, 10, somar);

#aqui ele passa os valores a serem somados e a função "subtrair" que subtrairá esses valores:
exibir_resultado(10, 10, subtrair);

#*args = tupla e **kwargs = dicionário




