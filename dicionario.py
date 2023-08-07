#exemplos de dicionario:
#exemplo 1:
cliente = {"nome" : "gabriel", "idade" : 26}

print(cliente);

#exemplo2: usando a classe "dict":
cliente = dict(nome = "Gabriel", idade = 26);

print(cliente);

#exemplo3: dicionário cliente já está criado:
cliente["idade"] = 26;

print(cliente);

#métodos da classe dict:
emails = {
    "gabrielpvl@hotmail.com":{"nome": "Gabriel", "telefone": "3245-6377"},
    "felipepvl@hotmail.com":{"nome": "Felipe", "telefone": "3245-77377"},
    "eduardopvl@hotmail.com":{"nome": "Eduardo", "telefone": "3245-8877"},
    "rimarpvl@hotmail.com":{"nome": "Gabriel", "telefone": "3245-6677"},
}

#método clear{}: ele apaga todos os valores do meu dicionário:
# emails.clear();

#método copy: aqui ele tira uma cópia do dicionário:
copia = emails.copy();

copia["gabrielpvl@hotmail.com"] = {"nome", "Biel"}

#aqui ele retorna do dicionário original os dados desse email:
print("dicionario original:\t", emails["gabrielpvl@hotmail.com"]);

#aqui ele retorna do dicionário copiado os dados desse email:
#vc utiliza essa cópia para nao alterar os valores do dicionário original:
print("dicionario copiado:\t", copia["gabrielpvl@hotmail.com"]);

#fromkeys{}
#aqui ele adiciona mais chaves no dicionário:

#antes de adionar:
dict.fromkeys(["nome", "telefone"]);
print(dict.fromkeys(["nome", "telefone"]));

#aqui foi adicionada uma chave a mais chamada "vazio":
dict.fromkeys(["nome", "telefone"], "vazio");

print(dict.fromkeys(["nome", "telefone"], "vazio"));

#get{}:
#se nao existir ele retorna "None":
print(emails.get("chave"));

#se nao existir ele retorna os dados:
print(emails.get("gabrielpvl@hotmail.com"));

#keys{}:
print("Keys:");
retorno = emails.keys();
print("Utilizando 'keys':\t",retorno);






