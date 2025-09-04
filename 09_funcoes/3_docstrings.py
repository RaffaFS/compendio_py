# Docstrings são basicamente strings de documentação
# Elas servem, por exemplo, para documentar uma função que será
# utilizada em outros documentos que não aquele onde foi criada

# Isso é útil e importante para que outras pessoas ou mesmo você
# do futuro possa saber com maior facilidade, como seu código
# funciona, já que tudo que você escrever nas docstrings de uma
# função poderá ser acessado por "help(função)"

def contador(i, f, p):
    """
        Faz uma contagem e mostra na tela.
        Parâmetro i: início da contagem
        Parâmetro f: fim da contagem
        Parâmetro p: passo da contagem
        
        Tenha um bom dia ^^
    """
    cont = i
    while cont <= f:
        print(f'{cont}', end='..')       # o end padrão é \n, reatribuindo o end consigo outra separação entre os prints sem pular linha
        cont += p
    print('Fim!')

help(contador)
contador(1,10,2)