# A modularização é basicamente a criação de módulos, ou seja documentos
# externos que armazenarão funções específicas que serão chamadas no nosso
# documento principal

# O objetivo é a divisão do código a fim de criar maior organização e
# legibilidade em grandes projetos

# Seria a ideia de ter 10 arquivos com 100 linhas cada ao invés de 1
# arquivo com 1000 linhas ou, de maneira mais metafórica, ter uma 
# mesa com 5 gavetas com ferramentas organizadas por tipo ou função
# ao invés de ter uma mesa sem gavetas onde tudo fica jogado no tampo

import util

print(util.som(8,4))
print(util.sub(8,4))
print(util.mul(8,4))
print(util.div(8,2))