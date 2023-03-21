login = ''
import json
from os import waitpid
# import pandas as pd

def menu_start(login_par):
    login = login_par
    
    commands = [orders, completed, salary]

    while True:
        print("-"*45)
        print("Welcome, dear waiter!")
        print("-"*45)
        print("Please dial the menu number to work with the program, if finished, then dial 5:") 
        print("-"*45)
        print('''Please choose: \n
        1 - Orders
        2 - Related orders
        3 - My salary
        5 - Exit\n
    ''')
        command = int(input(":")) # зп

        if(command>5 or command<1):
            print("-"*45)
            print("Error, there is no such command here, try again :-(")
            continue
        if(command == 5):
            break
        if(command == 1):
            orders()
        if(command == 2):
            completed()
        if(command == 3):
            salary()
def orders(): # читает заказы клиента
    # df = pd.read_csv('order.txt')
    # print(df)
    with open("order.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(lines)

    num = int(input("Choose which order you want to carry: ")) 
    print(lines[num]) # выбирает заказ, чтобы отнести

    with open('completed.txt','a',encoding='utf-8') as completed:
        completed.write(lines[num]) # отнесенный заказ записывается в другой файл

    def delete_line(file,num):
        lines = []
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
        with open(file,'w',encoding='utf-8') as f:
            for k,row in enumerate(lines):
                if(k!=num):
                    f.write(row)
    delete_line('order.txt',num)

def completed():
    with open("completed.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line)

def salary():
    with open("salarywaiter.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line)   

