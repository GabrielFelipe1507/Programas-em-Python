print("exemplo1: operadores aritméticos\n");
produto1 = 20;
produto2 = 10;

print("operações:");
print("soma=", produto1+produto2);
print("subtração=", produto1-produto2);
print("divisão=", produto1/produto2);
print("divisão inteira=", produto1//produto2);
print("multiplicação=", produto1*produto2);
print("resto da divisao=", produto1%produto2);
print("exponenciação=", produto1**produto2);

print("exemplo2: operadores de comparação\n");

saldo = 40;
saque = 20;

print("igual:", saldo== saque);
print("diferente:", saldo!=saque);
print("saldo maior?", saldo> saque);
print("saldo menor?", saldo<saque);
print("saldo maior igual?", saldo>=saque);
print("saldo menor igual?", saldo<=saque);

print("exemplo3: Operadores de atribuição:\n");

print("soma:\n");
saldo = 700;
saldo+=200;
print("subtração:\n");
saldo2 = 700;
saldo2-=200;
print("exponenciação:\n");
saldo3 = 3;
saldo3**= 2;
print("divisao:\n");
saldo4 = 3;
saldo4/= 2;
print("divisão inteira:\n");
saldo5 = 3;
saldo5//= 2;

print("resto da divisão:\n");
saldo6 = 6;
saldo6%= 2.5;

print("soma:\n");
print(saldo);
print("subtração:\n");
print(saldo2);
print("exponenciação:\n");
print(saldo3);
print("divisao:\n");
print(saldo4);
print("divisão inteira:\n");
print(saldo5);
print("resto da divisão:\n");
print(saldo6);

print("exemplo4: Operadores lógicos:\n");

saldo = 800;
saque = 100;
limite = 200;

print("Operador 'and':\n");
print("Verdade e Verdade = é verdadeiro quando utilizo o 'and'");
print(saldo > saque and saldo > limite);
print("Verdade e Falso = é falso quando utilizo o 'and'");
print(saldo > saque and saque > limite);
print("Falso e Verdadeiro = é falso quando utilizo o 'and'");
print(saldo < saque and saldo > limite);
print("Falso e Falso = é falso quando utilizao o 'and'");
print(saldo < saque and saldo < limite);

print("Operador 'or':\n");
print("Verdade e Verdade = é verdadeiro quando utilizo o 'or'");
print(saldo > saque or saldo > limite);
print("Verdade e Falso = é verdadeiro quando utilizo o 'or'");
print(saldo > saque or saque > limite);
print("Falso e Verdadeiro = é verdadeiro quando utilizo o 'or'");
print(saldo < saque or saldo > limite);
print("Falso e Falso = é falso quando utilizao o 'or'");
print(saldo < saque or saldo < limite);

print("exemplo5: Operadores de identidade:\n");

print("Strings:");
carro = "Gol g5";
nome_carro = carro;

print("Valores Inteiros:");
saldo, limite = 300, 400;

#aqui ele esta checando se a variavel carro está na mesma regiao de memória que a variável nome_carro:
print(carro is nome_carro);

#aqui ele esta checando se a variavel carro não está na mesma regiao de memória que a variável
#  nome_carro, portanto dará falso pois eles utilizam a mesma região de memória:
print(carro is not nome_carro);

#fazendo com valores inteiros:
print(saldo is limite);

print("exemplo6: Operadores de associação:\n");
#string 'Gol g5':
carro = "Gol g5";
#lista de strings:
pecas_de_carro=["virabrequim", "caixa de direção", "amortecedores"];
#lista de valores numericos:
valores = [2000, 1500, 1000];

#aqui esta dizendo se contem a palavra "gol" na variavel 'carro':
print("Gol" in carro);
#aqui esta falando se não contem a palavra "palio" na variavel 'carro':
print("palio" not in carro);
#mesma coisa para valores numericos:
print(300 in valores);




