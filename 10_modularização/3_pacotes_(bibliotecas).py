# No fim do documento anterior vimos um pouco sobre a criação de
# pacotes, mesmo que isso não tenha sido mencionado explicitamente

# Passamos a criar pacotes com o mesmo objetivo da criação de módulos
# mas fazemos isso quando temos muitos módulos que possuem muitas
# funções, ou seja, são necessários somente em projetos enormes

# Um pacote basicamente é uma pasta com vários módulos dentro dela
# Ou ainda, em casos maiores, uma pasta com várias pastas dentro
# e cada uma dessas com vários módulos, nesse caso sendo módulos
# dentro de um pacote dentro de outro pacote

# Sua invocação é feita com "from pacote import modulo"
# e aqui eu sempre utilizarei modulo.funcao(), não funcao() sozinha
# A não ser que faça como vimos no documento anterior "from pacote.modulo import funcao"

# Novamente bom lembrar que toda pasta que será um pacote precisará de um arquivo
# __init__.py dentro dela para se comportar da maneira adequada como pacote
# O arquivo __init__.py pode estar vazio