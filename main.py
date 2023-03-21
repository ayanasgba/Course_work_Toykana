import login, admin, manager, client, waiter

def main():
    result = login.menu_start()
    if(result[0]=='admin'):
        admin.menu_start(login)
    if(result[0]=='manager'):
        manager.menu_start(login)
    if(result[0]=='client'):
        client.menu_start()
    if(result[0]=='waiter'):
        waiter.menu_start(login)
main()
