# Python-JSON Login Page

## Purpose

An easy way of storing usernames and passwords to a simple database.
<p>//WARNING// This is not a secure way to store passwords due to their plaintext nature! The intent is purely to demonstrate the usefulness and relationship between python and JSON.</p>

## Skills Learned

- Read and write to JSON files using python
- JSON can only read certain serialized characters and characters encrypted with the Crypto library are unreadable which means storing secure passwords is impossible [Not a skill but I am still disappointed :( if there is a way around this please lmk.] 

## Tools

VS Code

## Process

Import modules and establish variables

```
import json
from time import sleep


jsonFile = open('password_List.json', 'r')
jsonData = jsonFile.read()
jsonObj = json.loads(jsonData)
```

Create the main function that will write to the JSON file

```
def write_Password(filename='password_List.json'):
    
    new_Username = input('Enter a username: ')
    new_Password = input('Enter a password: ')

    toAdd ={"username": (new_Username), "password": (new_Password)}

    with open(filename, 'r+') as file: 
        file_data = json.load(file)
        file_data["password_List"][0]["credentials"].append(toAdd)

        file.seek(0)
        json.dump(file_data, file, indent=4)
```

Create a login_Page() function and introduce the login page

```
def login_Page():
    
    jsonFile = open('password_List.json', 'r') #rereading the json file allows us to write a new login and then login to that account without closing the program
    jsonData = jsonFile.read()
    jsonObj = json.loads(jsonData)
    
    print(f'\___________________________/\n \n  Welcome to ABC123 Login Page! \n ___________________________ \n/                           \ ')

    sleep(2)

    inputted_Username = input('Enter your Username: ')
    inputted_Password = input('Enter your Password: ')

    stored_Passwords = (jsonObj["password_List"][0]["credentials"])
```

Within the login_Page() function, create a for loop to run through the items within the JSON file until the entered username can be matched with the stored one and the entered password can be compared with its associated stored one

```
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
```

Within the login_Page() function, create an alternate output for if the entered credentials are non-existent

```
if recognition == False:
        print ('The credentials you have entered are not on our system')
```

Create a while loop to check whether you already have an account. If yes then break to the login_Page() function, if no then run the write_Password() function before breaking to the login_Page() function

```
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
```
