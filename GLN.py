from os.path import exists
file_path = 'KA.xml'

def three():
    content = file.read()
    print(content[0])
def four ():
    content = file.readline()
    print(content)
def five ():
    content = file.read()
    print(content)
def six ():
    content = file.read()
    print(content)
def seven ():
    content = file.read()
    is_tag = True
    output = ""
    for i in content:
        if i == '<':
            is_tag = True
        if i == '>':
            is_tag = False
        if is_tag == False and i != '>':
            output += i
    print(output)
def eight ():
    content = file.read()
    is_tag = True
    output = ""
    for i in content:
        if i == '<':
            is_tag = True
        if i == ' ':
            is_tag = False
        if is_tag == False and i != ' ':
            output += i
    print(output) 
def nine ():
    content = file.read()
    is_tag = True
    output = ""
    for i in content:
        if i == '<':
            is_tag = True
        if i == ' ':
            is_tag = False
        if is_tag == False and i != ' ' and i != '>':
            output += i
    print(output) 
def ten ():
    content = file.read()
    is_tag = True
    output = ""
    for i in content:
        if i == '<':
            is_tag = True
        if i == ' ':
            is_tag = False
        if is_tag == False and i != ' ' and i != '>':
            output += i
    print(output) 
    with open('Ergebnis.txt','w') as file:
        file.write(output)      
def eleven ():
    content = file.read()
    search = input('Enter the search string: ')
    count = content.count(search)
    print(count)

if(exists(file_path)):
    with open('Menu.txt','r') as file:
        menu = file.read()
        print(menu)
    choose = input('Choose a number: ')
    with open(file_path,'r') as file:
        if choose == '3':
            three()
        elif choose == '4':
            four()
        elif choose == '5':
            five()
        elif choose == '6':
            six()
        elif choose == '7':
            seven()
        elif choose == '8':
            eight()
        elif choose == '9':
            nine()
        elif choose == '10':
            ten ()
        elif choose == '11':
            eleven()
    
else:
    print("Datei nicht vorhanden")

