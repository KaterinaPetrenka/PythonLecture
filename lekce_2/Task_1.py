#login
data = {
    'Jakub': 'heslo1',
    'Jana': 'heslo2',
    'Petr': 'heslo3',
}

username = input('Zadej username: ')
password = input('Zadej password: ')

print(username, password)

error_text = 'prihlaseni se nepodarilo'

# if username in data:
#     if password == data[username]:
#         print('OK')
#     else:
#         print(error_text)
# else:
#     print(error_text)


try:
    assert data[username] == password
    print('OK')
except:
    print(error_text)
