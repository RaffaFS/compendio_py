# O python é uma linguagem que trabalha a partir de pacotes de módulos,
# alguns já são pré instalados, mas se quisermos funcionalidades mais
# específicas podemos instalar módulos extras.

# O python "não vem completo" para que não gastemos memória sem necessidade,
# importando então módulos apenas quando necessário.

# Um módulo então em resumo é um arquivo .py que pode conter funções,
# classes e variáveis e que pode ser chamado através de "import" em 
# outro arquivo

# Um conjunto de módulos é chamado de biblioteca, e a única diferença
# é realmente essa, um é singular, o outro é plural. A forma de importação
# é a mesma, chamando a biblioteca através de "import"


###############################
##### FAZENDO IMPORTAÇÕES #####
###############################

# Geralmente importaremos um módulo solto se esse for nossa própria criação
# do contrário, costumamos importar bibliotecas inteiras ou módulos de
# dentro dessas bibliotecas, então existem duas maneiras de realizar essa
# importação, e para cada caso existe uma maneira dee realizar o uso

# importando biblioteca time
import time
time.sleep(3)
print('Olá mundo')
# no caso acima, como importamos a biblioteca inteira, a cada uso temos que
# chamar "biblioteca.módulo()"

# importando módulo sleep que pertece a biblioteca time
import sleep from time
sleep(3)
print('Olá mundo')
# no caso acima, como importamos apenas um módulo da biblioteca time, chamamos
# apenas "módulo()", porém outros módulos de time não estarão disponíveis,
# podendo, caso sejam necessários, serem importados um a um da mesma forma