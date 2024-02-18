import json
from time import sleep


jsonFile = open('password_List.json', 'r')
jsonData = jsonFile.read()
jsonObj = json.loads(jsonData)


def write_Password(filename='password_List.json'):
    
    new_Username = input('Enter a username: ')
    new_Password = input('Enter a password: ')

    toAdd ={"username": (new_Username), "password": (new_Password)}

    with open(filename, 'r+') as file: 
        file_data = json.load(file)
        file_data["password_List"][0]["credentials"].append(toAdd)

        file.seek(0)
        json.dump(file_data, file, indent=4)


def login_Page():
    
    jsonFile = open('password_List.json', 'r') #rereading the json file allows us to write a new login and then login to that account without closing the program
    jsonData = jsonFile.read()
    jsonObj = json.loads(jsonData)
    
    print(f'\___________________________/\n \n  Welcome to ABC123 Login Page! \n ___________________________ \n/                           \ ')

    sleep(2)

    inputted_Username = input('Enter your Username: ')
    inputted_Password = input('Enter your Password: ')

    stored_Passwords = (jsonObj["password_List"][0]["credentials"])

    recognition = False

    for data in stored_Passwords: #loops through credentials area of password list looking for the passed username, if found the password is pulled
        if data['username'] == (inputted_Username):
            associated_Password = (data['password'])
            recognition = True
            if associated_Password == inputted_Password:
                print ('Login Successful')
        elif data['username'] == (inputted_Username):
            associated_Password = (data['password'])
            recognition = True
            if associated_Password != inputted_Password:
                print ('Login Failed')
        
    if recognition == False:
        print ('The credentials you have entered are not on our system')


while True:
    determine = input('Do you already have an account? ')
    if determine.lower() == 'yes':
        break
    elif determine.lower() == 'no':
        write_Password()
        break
    else:
        print('Bad input')
        

login_Page()