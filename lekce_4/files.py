#lecture_4
#files.py
#prace se soubory

def read():
    with open('lekce_4/soubor.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end=' ')
read()
#file.readline() - reads 1 line
#file.read() - full file
# prints line by line

#write - always deletes the existing content and adds a new content
def write():
    with open('lekce_4/soubor.txt', mode='w', encoding='utf-8') as file:
        file.write('Colorfull')
write()

#append - always will add a new lines to a new file test2.txt
def append():
    with open('lekce_4/test2.txt', mode='a', encoding='utf-8') as file:
        file.write('Im fond of Python\n')
append()