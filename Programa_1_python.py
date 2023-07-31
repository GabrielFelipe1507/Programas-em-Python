
print("\n************Aula 1: Print************");
print("oi, Seja Bem Vindo ao Curso de Python");

print("\n************Aula 2: Tipo de Dados************");
print("Tipo Numeros Inteiros =",1+10);
print("Tipo Numeros Inteiros =",11 + 10 + 1000);
print("Tipo Numeros de Ponto FLutuante(float):1.5 + 0.5 =", 1.5 + 0.5)
print("Tipo Boolean=", True);
print("Tipo Boolean=", False);
print("Tipo String - 'Python'");

print("\n************Aula 3: Variáveis e Constantes************");
nome = "Gabriel Felipe"
idade = 27
print(nome, idade);

print("Constantes:");
BRAZILIAN_STATES = ["SP", "RJ", "MS", "MT", "MG", "PR", "AM", "BA"]
print("Em python constantes podem ser alteradas")
print(BRAZILIAN_STATES);

BRAZILIAN_STATES = 10
print("Empython constantes podem ser alteradas - Constante Alterada:")
print(BRAZILIAN_STATES);

print("\n************Aula 4: Conversão de Tipos************");

print("de float para inteiro e vice-e-versa:\n");
preco = 10;
print("numero sem ser convertido=", preco);
preco_quebrado = float(preco);
print("numero convertido em 'float'=", preco_quebrado);

print("\nde numero quebrado(float) para inteiro novamente:");
preco_quebrado = int(preco);

print("numero convertido em 'inteiro'=", preco_quebrado);
print("de numerico para string concatenando:\n");
preco = 10.50
idade= 32

print(str(preco));
print(str(idade));

print("\nConversão de uma String do tipo float e do tipo int:");
print("Aqui abaixo era um numero quebrado e deu '1' como resultado pois,"
      + " converti utilizando (int), então ele contara somente uma casa antes da virgula");
print(int(1.973487));
print("Tipo Int:")
print(int("10"));
print("Tipo Float:")
print(float("10.10"));

print("Convertendo p/ String e perguntando o Tipo da variável utilizando o 'type':");
valor = 10;
valor_str= str(valor);
print(type(valor));
print(type(valor_str));

print("\n************Aula 5: Funções de entrada e saída************");

nome = input("Informe seu nome: ");
idade = input("Informe a sua idade: ");

print(nome);
print(idade);

