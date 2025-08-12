# Como em qualquer outra linguagem de programação, uma variável segue sendo uma variável
# Um bloco de memória mutável com valor alocado, a diferença é que não preciso definir "var" ou "let"
# Basta apenas passar o nome do dado e em seguida o valor do mesmo

nome = "andre"
idade = 30
print(nome)
print(idade)
print("//////////////////////////////////////////////////")


nome = "Bruno"
idade = 20
print(nome)
print(idade)
print("//////////////////////////////////////////////////")


# Assim como o JS, o Python também é uma linguagem com tipagem dinâmica, 
# mas abaixo vamos entender quais são os tipos nativos do python com a
# ajuda da função "type" que trará no terminal o tipo do dado invocado

# (int) tipo numérico inteiro
preco1 = 100
tipo_preco1 = type(preco1)
print(preco1)
print(tipo_preco1)
print("//////////////////////////////////////////////////")

# (float) tipo numérico decimal
preco2 = 97.90
tipo_preco2 = type(preco2)
print(preco2)
print(tipo_preco2)
print("//////////////////////////////////////////////////")

# Acima fiz o armazenamento dos tipos dos meus dados em outro dado, outra variável
# Note que abaixo farei uso de type diretamente no print sem armazená-lo

# (str) tipo texto string
pais = "Brasil"
print(pais)
print(type(pais))
print("//////////////////////////////////////////////////")

# (bool) tipo lógico booleano
# em sua declaração de valor a primeira letra deve ser maiúscula
usuario_maior_de_idade = False
print(usuario_maior_de_idade)
print(type(usuario_maior_de_idade))
print("//////////////////////////////////////////////////")

# (NoneType) tipo vazio
# um tipo vazio é ainda um dado com valor, o valor "vazio"
# não confunda com um dado inexistente.
# Para tipo "NoneType" pode-se imaginar basicamente um campo de input que não foi preenchido
# E esse "não preenchimento", esse "vazio", é um valor aceito e importante de se saber
telefone_fixo = None
print(telefone_fixo)
print(type(telefone_fixo))
print("//////////////////////////////////////////////////")