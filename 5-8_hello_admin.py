usernames=['admin','service','clinical','physicist','engineer','nurse']
log_attempt = 0
log_status = False

while log_attempt < 3 and log_status == False:

    log = input("Type your log : ")

    if log in usernames:


        if log == 'admin':
            print(f"Welcome, you are logged as administrator.")
        elif log == 'service':
            print(f"Welcome, you are logged in {log.title()} mode.")
        elif log == 'clinical':
            print(f"Wecome, you are logged in {log.title()} mode.")
        elif log == "physicist":
            print(f"Wecome Dear {log.title()} !")
        elif log == 'engineer':
            print(f"Welcome Dear {log.title()} !")
        elif log == 'nurse':
            print(f"Welcome Dear {log.title()} !")

        log_status = True

    else:
        print(f"Log not valid, try again...")
        log_attempt += 1

if log_status == False :
    print("logon failed, contact your administrator !")


