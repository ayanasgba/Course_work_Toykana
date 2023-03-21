login = ''

def menu_start(login_par):
    login = login_par

    commands = [user_control, events_control, report]

    while True:
        print("-"*45)
        print("Welcome, dear admin!")
        print("-"*45)
        print("Please dial the menu number to work with the program, if finished, then dial 5: ") 
        print("-"*45)
        print('''Please choose: \n
        1 - User control
        2 - Events control
        3 - Report
        5 - Exit\n
    ''')
        
        command = int(input(":")) # выбирает один вариант из меню

        if(command>5 or command<1):
            print("-"*45)
            print("Error, there is no such command here, please try again :-(") # если команде вне диапазона, то продолжается
            continue
        if(command == 5): # если выбирает команду для выхода, то прерывается
            break
        if(command == 1): # вызывается функция управления пользователями
            user_control()
        if(command==2): # вызывается функция управления мероприятиями
            events_control() 
        if(command==3): # вызывается функция отчета
            report()

def user_control():
        print("-"*45)
        user_management = int(input('''Please choose: 
        1 - add user
        2 - delete user
        3 - rename user
        0 - exit to the main menu\n'''))
        print("-"*45)

        if user_management == 1: 
            with open('login.txt','a', encoding='utf-8') as f: # файл, где хранятся логины и пароли всех пользователей
                username = input('Enter username: ') # пишет логин пользователя, которого хочет добавить
                password = input('Enter password: ') # пишет пароль пользователя, которого хочет добавить
                type_of_ac = input('Enter the type of account: ')  # пишет тип аккаунта пользователя, которого хочет добавить
                field = username + ' ' + password + ' ' + type_of_ac  # сохраняется а файле, в таком порятке(логин, пароль, тип аккю)
                print(field)
                f.write(field) 

        if user_management == 2:  # команда для удаления пользователя
            with open("login.txt", "r", encoding='utf-8') as f:
                lines = f.readlines() # читает файл, где хранятся логины и пароли всех пользователей

            with open('login.txt', "w", encoding='utf-8') as f: # файл, где хранятся логины и пароли всех пользователей
                delete_name = input('Enter the name of the user you want to delete: ') # пишет логин пользователя, которого хочет удалить
                delete_acc = input('Enter the password of the user you want to delete: ') # пишет пароль пользователя, которого хочет удалить
                flag = True
                for line in lines:
                    if delete_name and delete_acc not in line:
                        f.write(line)
                        flag = False
                        print('User deleted.')
                if flag:
                    print('This user does not exist.') # если такого пользователя нет

        if user_management == 3: # команда для переименования пользователей
            with open ('login.txt', 'r', encoding='utf-8') as f:
                old_data = f.read()
                old_username = input('Enter the user you want to change: ')
                new_username = input('Enter what to change to: ')
                new_data = old_data.replace(old_username, new_username)

            with open ('login.txt', 'w', encoding='utf-8') as f: # записывается новое значение
                print('Successfully changed.')
                f.write(new_data)
    
def events_control():
        event_management = int(input('''Please choose: 
        1 - add event
        2 - delete event
        3 - rename event 
        0 - exit to the main menu\n'''))

        if event_management == 1: # команда для добавления нового мероприятия
            with open('events.txt','a', encoding='utf-8') as f: 
                eventname = input('Enter the name of the event: ')
                field = eventname
                print(field)
                f.write(field)

        if event_management == 2: # команда для удаления мероприятия
            f = open("events.txt", "r+", encoding="utf-8")
            lines = f.readlines()
            print(f.read())
            f.close()

            with open('events.txt', "w", encoding='utf-8') as f: 
                delete_event = input('Enter the name of the event you want to delete: ')
                flag = True
                for line in lines:
                    if delete_event not in line:
                        f.write(line)
                        flag = False
                        print('The event has been deleted.')
                if flag:
                    print('There is no such event. ')

        if event_management == 3: # команда для переименования мероприятия
            with open ('events.txt', 'r', encoding='utf-8') as f:          
                old_data = f.read()
                old_username = input('Enter the user you want to change: ')
                new_username = input('Enter what to change to: ')
                new_data = old_data.replace(old_username, new_username)

            with open ('events.txt', 'w', encoding='utf-8') as f:
                print('Successfully changed.')
                f.write(new_data)
    
def adress():
        adress_management = int(input('''Please choose: 
        1 - add new address
        2 - delete the adress
        3 - change address 
        0 - exit to the main menu\n'''))

        if adress_management == 1: # команда для добавления нового адреса
            with open('adress.txt','a', encoding='utf-8') as f: 
                eventname = input('Enter the address: ')
                field = eventname
                print(field)
                f.write(field)

        if adress_management == 2: # команда для удаления мероприятия
            f = open("adress.txt", "r+", encoding="utf-8")
            lines = f.readlines()
            print(f.read())
            f.close()

            with open('adress.txt', "w", encoding='utf-8') as f: 
                delete_event = input('Enter the address you want to delete: ')
                flag = True
                for line in lines:
                    if delete_event not in line:
                        f.write(line)
                        flag = False
                        print('The address has been deleted.')
                if flag:
                    print('There is no such address.')

        if adress_management == 3: # команда чтобы поменять адрес
            with open ('adress.txt', 'r', encoding='utf-8') as f:
                old_data = f.read()
                old_username = input('Enter the address to be changed: ')
                new_username = input('Enter what to change to: ')
                new_data = old_data.replace(old_username, new_username)

            with open ('adress.txt', 'w', encoding='utf-8') as f:
                print('Successfully changed')
                f.write(new_data)

def report():
    print("-"*40)
    print("Total amount for the event: ") # общая сумма за мероприятие
    with open("sum.txt", "r") as f:
        for line in f:
            print(line)

    print("-"*40)
    print("Waiter's salary: ") # зарплата официанта
    with open("salarywaiter.txt", "r") as f:
        for line in f:
            print(line)

    print("-"*40)
    print("Manager's salary: ") # зарплата менеджера
    with open("salaryman.txt", "r") as f:
        for line in f:
            print(line)

    print("-"*40)
    print("Net profit: ") # чистая прибыль
    with open("sumch.txt", "r") as f:
        for line in f:
            print(line)


    


