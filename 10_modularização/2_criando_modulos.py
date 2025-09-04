# A modularização é basicamente a criação de módulos, ou seja documentos
# externos que armazenarão funções específicas que serão chamadas no nosso
# documento principal

# O objetivo é a divisão do código a fim de criar maior organização e
# legibilidade em grandes projetos

# Seria a ideia de ter 10 arquivos com 100 linhas cada ao invés de 1
# arquivo com 1000 linhas ou, de maneira mais metafórica, ter uma 
# mesa com 5 gavetas com ferramentas organizadas por tipo ou função
# ao invés de ter uma mesa sem gavetas onde tudo fica jogado no tampo

# Outras vantagens são a facilidade na manutenção, a ocultação do
# código detalhado e a possibilidade de reutilização em outros arquivos

import util

print(util.som(8,4))
print(util.sub(8,4))
print(util.mul(8,4))
print(util.div(8,2))

# Como pode ver funciona da mesma maneira que a importação de módulos
# presentes em python, e se eu quisesse uma única função bastaria fazer
# o mesmo que vimos também no documento anterior:

from util import sub                                # por exemplo

# O importante é que o módulo ou biblioteca esteja no mesmo diretório
# do arquivo que está chamando ele

# Caso o módulo ou biblioteca esteja em subpastas o ideal é:
# 1. Em cada subpasta que precise ser acessada deve ser criado um arquivo "__init__.py"
# 2. Em seguida cria-se na mesma pasta o arquivo com os códigos (arquivo módulo)
# 3. Invoca o módulo: "from pasta1.pasta2.pasta3 import módulo"
# 3. Exemplo prático: "from src.app.modulos import util"