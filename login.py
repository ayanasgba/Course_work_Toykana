def menu_start():
    print("*"*40)
    print("Welcome to the 'Diamond' restaurant!")
    print("*"*40)
    lines = []
    account_types = ["admin","manager","client","waiter"] # выбирает один тип аккаунта
    enter_choice = input("1. Sign in \ 2. Sign up - ") 
    if enter_choice == '2':
        register()
    with open('login.txt', encoding='utf-8') as file: 
        lines = file.readlines()
    while True :
        for i in account_types:
            print(i,'\n')
        print("*"*40)
        account_type_input = input("Enter your account type: ")
        if not(account_type_input in account_types):
            print("This type of account is not available.") # если такого аккаунта нет
            print("*"*40)
            continue 
        login = input("Enter login - ")
        print("*"*40)
        password = input("Enter password - ")
        result = sign_in(login,password,account_type_input,lines)
        if(result):
            return[account_type_input.lower(),login]
        else:
            print("Wrong")
            print("*"*40)
        sign_in(result)


def sign_in(login, password, account_type, lines):
    for line in lines:
        line = line.split()
        if(line[0]==login and line[1]==password and line[2]==account_type.lower()):
            print("The authorization was successful. ") # при успешном входе
            print("*"*40)
            return True
    return False

def register():
    account_types = ["admin","manager","client","waiter"]
    account_type_input = input("Enter the type of account: ")
    print("*"*40)
    if not(account_type_input.lower() in account_types):
        print("This type of account is not available.")
        return
    login = input("Enter login - ")
    print("*"*40)
    password = input("Enter password - ")
    print("*"*40)
    print("The registration was successful.") # при успешном прохождении регистрации

    with open('login.txt','a', encoding='utf-8') as file: # записывается в файл
        file.write(f"{login} {password} {account_type_input}\n")

if __name__ == '__main__':
    menu_start()