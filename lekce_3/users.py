# users.py

import os, json

DATA_PATH = 'Python2024/lekce_3/users.json'

def read_data():
    with open(DATA_PATH, encoding ='utf-8') as file:
        return json.load(file)
     
    data = read_data()

def write_data(data):
     with open(DATA_PATH, mode="w", encoding='utf=8') as file:
        json.dump(data, file)#zapis do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshoduji')

def check_username(data, username):
    if username in data:
        raise ValueError ('Uzivatel jiz existuje')


def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data [username] = password
    write_data(data)

    

def login(username, password):
    data = read_data()
    try:
        assert data[username]==password, 'Chybne heslo'
        return True
    except (KeyError, AssertionError):
        return False


def change_password(old_password, password, password_repeat):
    pass


    # 1.json
    # 2.najdeme ho pokud ho najdeme
    # 3. smayeme
    # 4. ulozime DATA_PATH

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)


#change_password
#logout
#register
#controla

delete_user('test1', 'heslo1')