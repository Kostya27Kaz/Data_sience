parol = {'Olga':'Дзержинского'}

while True:
    login = input('Введите логин: ')
    if login in parol:
        password = input('Введите пароль: ')
        if password == parol[login]:
            print ('Welcome')
            break
        else:
            print('Неправильный пароль')
    else:
        print('Неправильный логин')
            

