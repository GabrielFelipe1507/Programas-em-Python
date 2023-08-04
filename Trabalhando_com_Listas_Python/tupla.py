# a diferença da trupla para lista é que ela não pode ser 
# alterada (seus valores) até o final do programa:
# trabalhando com tuplas:
# exemplo abaixo de uma tupla:
frutas = ("laranja", "pera", "uva",);

letras = tuple("python");

numeros = tuple([1, 2, 3, 4]);

pais = ("Brasil",)

#aqui está uma tupla dentro da outra:

carros = (
    (1, "gol", 2),
    ("celta", 2, 3),
    (4, 2, "astra"),
);
#printando as posições da tupla:
print(carros[0]);
print(carros[1][0]);



