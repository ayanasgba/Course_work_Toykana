login = ''

def menu_start(login_par):
    login = login_par
    
    commands = [order_control, events_control, salary_control, completed_orders]

    while True:
        print("-"*45)
        print("Welcome, dear manager!")
        print("-"*45)
        print("Please dial the menu number to work with the program, if finished, then dial 5:") 
        print("-"*45)
        print('''Please choose: \n
        1 - Orders control
        2 - Events control
        3 - Salary
        4 - Related orders
        5 - Exit\n
    ''')
        
        command = int(input(":"))

        if(command>5 or command<1):
            print("-"*45)
            print("Error, there is no such command here, try again :-(")
            continue
        if(command == 5):
            break
        if(command == 1):
            order_control()
        if(command == 2):
            events_control()
        if(command == 3):
            salary_control()
        if(command == 4):
            completed_orders()
            
def order_control(): # читает файл с заказами клиента
    with open("order.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line)

def events_control():
        event_management = int(input('''Please choose: 
        1 - add event
        2 - delete event
        3 - rename event 
        0 - exit to the main menu\n'''))

        if event_management == 1:
            with open('events.txt','a', encoding='utf-8') as f: 
                eventname = input('Enter the name of the event: ')
                field = eventname
                print(field)
                f.write(field)

        if event_management == 2:
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

        if event_management == 3:
            with open ('events.txt', 'r', encoding='utf-8') as f:
                old_data = f.read()
                old_username = input('Enter the user you want to change: ')
                new_username = input('Enter what to change to: ')
                new_data = old_data.replace(old_username, new_username)

            with open ('events.txt', 'w', encoding='utf-8') as f:
                print('Successfully changed.')
                f.write(new_data)

def salary_control():
    with open("sum.txt", "r") as f: # берет общую сумму и вычисляет зарплату официанта и менеджера
        for line in f:
            print(line)

    aa = int(line)
    service = (aa*10)/100
    man = (aa*12)/100
    aaa = aa-service-man

    print("Left: ", aaa, "\nWaiter's salary: ", service, "\nManager's salary: ", man )

    with open("salarywaiter.txt", "a") as f:
        b = f.write('\n')
        a = f.write(str(service))
    with open("salaryman.txt", "a") as f:
        b = f.write('\n')
        a = f.write(str(man))
    with open("sumch.txt", "a") as f: # передает чистую прибыль в другой файл
        b = f.write('\n')
        a = f.write(str(aaa)) 

def completed_orders(): # читает файл с отнесенными заказами
    with open("completed.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line)