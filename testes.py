with open('exemplo.txt', 'a+') as f:
    f.seek(0)
    ola = f.read()
    print(ola)