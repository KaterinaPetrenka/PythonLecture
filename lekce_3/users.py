#lecture_3
# users.py

import os, json, hashlib

DATA_PATH = 'Python2024/lekce_3/users.json'

def hash_password(password):
    hash_value = hashlib.sha256(password.encode())
    return hash_value.hexdigest()

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
    data [username] = hash_password(password)
    write_data(data)

    

def login(username, password):
    data = read_data()
    try:
        assert data[username]== hash_password(password), 'Chybne heslo'
        return True
    except (KeyError, AssertionError):
        return False

############## homework
def change_password(username, password_repeat):
    data = read_data()
    if username not in data:
        raise ValueError('Uzivatel neexistuje')
    
    if data[username] != password_repeat:
        raise ValueError('Chybne heslo')
###############

    # 1.json
    # 2.najdeme ho pokud ho najdeme
    # 3. smayeme
    # 4. ulozime DATA_PATH

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == hash_password(password):
        del data[username]
        write_data(data)



        #tests

        def test():
            #register('test123', 'heslo', 'heslo')
            print(login('heslo', 'Python'))
            print(login('test', 'heslo'))
            delete_user('test', 'hesloooaaaaa')
            change_password('test', 'heslo', 'new_pass', 'new_pass')

        def test2():
            register(login('heslo', 'Python', 'Python'))



#change_password
#logout
#register
#controla
