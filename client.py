import json
import pandas as pd

with open('menu.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
first = data.get("first", [])
second = data.get("second", [])
salads = data.get("salads", [])
drinks = data.get("drinks", [])
tea = data.get("tea", [])


df = pd.read_csv('month_january.csv')
df1 = pd.read_csv('resert.csv')
df.index += 1
df1.index += 1


def menu_start():
    commands = [show_menu, abc, order, ch_adress]
    while True:
        print("-"*45)
        print("Welcome to the 'Diamond' restaurant, dear client!")
        print("-"*45)
        print("Please dial the menu number to work with the program, if finished, then dial 5:") 
        print("-"*45)
        print('''Please choose: \n
        1 - Select date
        2 - View Menu
        3 - Checkout
        4 - Choose an address
        5 - Exit\n
    ''') 
        command = int(input(": "))
        
        if(command>5 or command<1):
            print("-"*45)
            print("Error, there is no such command here, please try again :-(")
            continue
        if(command == 5):
            break
        if(command == 1):
            abc()
        if(command == 2):
            show_menu()
        if(command == 3):
            order()
        if(command == 4):
            ch_adress()

def add():
    ask = input('Enter the order you want to cancel: ') # для отмены бронированного дня
    with open('month_january.csv', 'a+') as f: # берет значение которое хранится в файле бронированных дней
        with open('resert.csv') as ff:         # записывает туда, где он был изначально
            reader = ff.readlines()
            for row in reader:
                if ask in row:
                    f.write(row)
                    f.write('\n')

    with open("resert.csv", "w") as f:
        for row in reader:
            if not (ask in row):
                f.write(row)  

def abc():
    a2 = input('Enter to work with the menu 1) select a day 2) view the ordered days 3) cancel the ordered days: ')
    if a2 == '1':
        asc = input('Enter the month (order is made in advance up to 2 months :)').lower()
        if asc == 'january': 
            month = input('Enter the day:')
            with open('resert.csv', 'a+') as f:
                with open('month_january.csv') as ff:
                    reader = ff.readlines()
                    for row in reader:
                        if month in row:
                            f.write(row)
                            f.write('\n')

            with open("month_january.csv", "w") as f:
                for row in reader:
                    if not (month in row):
                        f.write(row)
            abc()
        elif asc == 'february':
            month = input('Enter the day: ')
            with open('resert.csv', 'a+') as f:
                with open('month_february.csv') as ff:
                    reader = ff.readlines()
                    for row in reader:
                        if month in row:
                            f.write(row)
                            f.write('\n')

            with open("month_february.csv", "w") as f:
                for row in reader:
                    if not (month in row):
                        f.write(row)
            abc()
        else:
            abc()
    elif a2 == '2':
        df1 = pd.read_csv('resert.csv')
        print(df1)
        abc()

    elif a2 == '3':
        df2 = pd.read_csv('resert.csv')
        print(df2)
        add()
        a = pd.read_csv('month_january.csv')
        print(a)
        a3 = pd.read_csv('month_january.csv')
        print(a3.sort_values(by=['Day']))
        abc()

def show_menu():
    print("First dishes: ")
    print("-"*45) 
    for item in first: # берет из json файла значения, 1-номер, 2-название блюда, 3-цену
        print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
    print("-"*45)
    print("Second dishes: ") 
    for item in second:
        print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}') 
    print("-"*45)          
    print("Salads: ")
    for item in salads:
        print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}') 
    print("-"*45)
    print("Drinks: ")
    for item in drinks:
        print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')    
    print("-"*45)                    
    print("Tea: ")
    for item in tea:
        print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}') 
        
def order():
    print("-"*40)
    people = int(input("Please enter the number of people:"))
    print("Event: ")
    with open('events.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
    event_order = int(input("What event do you want to host: "))
    print("-"*40)
    ev= {1:"1. Wedding\n", 2:"Kyz uzatuu\n", 3:"Sunnot toy\n", 4:"Tushoo kesuu\n", 5:"Anniversary\n",6:"Kuran okutuu\n", 7:"Corporate party\n"}
    order_first = int(input("First dishes: "))
    print("-"*40)
    a = {1:"Lentil soup\n", 2:"Meatball soup\n", 3:"Santavro\n", 4:"Kazakh meat\n",5:"Mastava\n", 6:"Chuchvara\n", 7:"Soup\n", 8:"Green cabbage soup\n", 9:"Vegetable soup\n", 10:"Lagman\n" }
    order_first_por = int(input("How many servings: "))

    order_second = int(input("Second dishes: "))
    print("-"*40)
    b = {1:"Fricassee with rice\n", 2:"Beef stroganoff with garnish\n", 3:"Chicken breast with creamy sauce\n", 4:"Fish in sauce\n", 5:"Chicken in sauce\n", 6:"Fried manti\n", 7:"Chaseji with chicken\n", 8:"Kazan trout kebab\n", 9:"Kuurdak with shin\n", 10:"Beshbarmak\n"}
    order_second_por = int(input("How many servings: "))

    order_salads= int(input("Salads: "))
    print("-"*40)
    order_salads_por = int(input("How many servings: "))
    c = {1:"Fattoush salad\n", 2:"Quinoa and Trout Salad\n", 3:"Homemade salad\n", 4:"Caesar Salad\n", 5:"Yerofeyevsky salad\n", 6:"Mushuru salad\n", 7:"Oriental Salad\n", 8:"Liansai salad\n", 9:"Greek Salad\n", 10:"Olivier salad\n"}

    order_drinks= int(input("Cold drinks: "))
    print("-"*40)
    order_drinks_lit = int(input("How many liters: "))
    d = {1:"Сoca Cola\n", 2:"Fanta\n", 3:"Sprite\n", 4:"Pepsi\n", 5:"Lemonade Black Currant\n", 6:"Homemade compote\n", 7:"Mineral water\n"}

    order_tea= int(input("Tea: "))
    print("-"*40)
    order_tea_por = int(input("How many teapots: "))
    e = {1:"Bay tea\n", 2:"Kyrma tea\n", 3:"Fruit tea\n", 4:"Tashkent tea\n", 5:"Tea with milk\n", 6:"Ginger tea\n", 7:"Black tea\n", 8:"Karkade\n", 9:"Rosehip\n", 10:"Issyk-Kul tea\n"}

    with open('order.txt','a', encoding='utf-8') as f: # записывает заказы на отдельном файле
        field = ev.get(event_order) + a.get(order_first) + b.get(order_second) + c.get(order_salads) + d.get(order_drinks) + e.get(order_tea) 
        # print(field)
        f.write(field)
    for item in first:
        if item["id"] == order_first: # ищет заказпо номеру(айди), принтует заказ
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
            break
    a = item.get("price")*order_first_por # считает сумму за первые блюда
    for item in second:
        if item["id"] == order_second:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
            break
    b = item.get("price")*order_second_por # считает сумму за вторые блюда
    for item in salads:
        if item["id"] == order_salads:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
            break
    c = item.get("price")*order_salads_por # считает сумму за салаты
    for item in drinks:
        if item["id"] == order_drinks:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
            break
    d = item.get("price")*order_drinks_lit # считает сумму за напитки
    for item in tea:
        if item["id"] == order_tea:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
            break
    e = item.get("price")*order_tea_por # считает сумму за чаи

    print("First dishes:",a)
    print("Second dishes:",b)
    print("Salads:",c)
    print("Cold drinks:",d)
    print("Tea:",e)
    all = a+b+c+d+e # вычисляет общую сумму
    print("-"*40)
    print("Amount: ", all)
    service = (all*15)/100 # вычисляет деньги за обслуживание
    print("-"*40)
    print("For the service (15%): ", service)
    print("-"*40)
    aaa = "Amount with service: ", all+service # вычисляет общую сумму с обслуживанием
    print(aaa)
    zadatok = int(input("Dear client, leave a deposit: ")) # просит у клиента оставить задаток
    print("-"*40)
    print("Total amount: ", all+service-zadatok) # вычисляет сумму, которую должен оплатить клиент
    print("-"*40)
    print("Number of guests: ", people) # принтует количество гостей
    with open("sum.txt", "a+") as f:
        f.write(str(all))

def ch_adress():
    print("-"*40)
    print("Adresses: ") # читает файл, где хранятся адреса
    with open('adress.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)

    ad= {1:"1.Maldybaeva 34B\n", 2:"Kievskay 9\n", 3:"Manasa 10\n"}
    order_adress = int(input("Select an address: ")) # выбирает адрес

    with open('order.txt','a', encoding='utf-8') as f: 
        field = ad.get(order_adress) +'\n' 
        print(field)
        f.write(field)

    





























