def titles (message, color = 'BLUE', tam = int(35)):
    global tamanho
    tamanho = tam
    colors('-'*tamanho, color)
    colors(f'{str(message).upper().center(tamanho)}',color)
    colors('-'*tamanho, color)
    return

def colors(message, color):
    if color == 'BLUE':
        print(f"\033[1;34m{message}\033[m")
    elif color == 'YELLOW':
        print(f"\033[1;33m{message}\033[m")
    elif color == 'RED':
        print(f"\033[1;31m{message}\033[m")
    elif color == 'GREEN':
        print(f"\033[1;32m{message}\033[m")
    elif color == 'MAGENTA':
        print(f"\033[1;35m{message}\033[m")
    elif color == 'CYAN':
        print(f"\033[1;36m{message}\033[m")
    return

def menu():
    print()
    titles('MENU')
    print("""[1] - Add a contact
[2] - See all contacts
[3] - Edit a contact
[4] - To favorite a contact
[5] - See only favorite contacts
[6] - Delete a contact
[7] - Exit""")
    colors('-'*tamanho,'BLUE')

    return

def add_contact (list, name, phone, email, favorited):
    list.append({
                "name": name,
                 "phone": phone,
                 "e-mail": email,
                 "favorite": favorited
                 })
    colors(f"\n{str(name).upper()} was added!",'GREEN')
    colors('-'*tamanho, 'GREEN')
    return  
    
def see_contacts(list, message, favorite = False, color = 'BLUE'):
    if not favorite:
        titles(f'{message}',color , tam = int(83))
        print(f'\033[1m{"INDEX":<10}{"NAME":<20}{"PHONE":<15}{"E-MAIL":<30}{"FAVORITE"}\033[m')
        for index, v in enumerate(list,start=1):
            print(f" [{index}]{"":<6}{v["name"]:<20}{v["phone"]:<15}{v["e-mail"]:<30}{v["favorite"]:^8}")
        colors('-'* tamanho, color)
        print()
    else:
        titles(f'{message}', color, tam = int(83))
        print(f'\033[1m{"INDEX":<10}{"NAME":<20}{"PHONE":<15}{"E-MAIL":<30}{"FAVORITE"}\033[m')
        for index, v in enumerate(list,start=1):
            if v["favorite"] == 'Y':
                print(f" [{index}]{"":<6}{v["name"]:<20}{v["phone"]:<15}{v["e-mail"]:<30}{v["favorite"]:^8}")
        colors('-'* tamanho, color)
        print()

    return

def edit_contacts(list, index, name, phone, email, favorited):
    list[index]["name"] = name
    list[index]["phone"] = phone
    list[index]["e-mail"] = email
    list[index]["favorite"] = favorited
    colors(f'\nContact updated!','YELLOW')
    return

def edting_some_info (list, index, info_check, new_info):
    if info_check == 'name':
        new_info = str(new_info).title()
    elif info_check == 'favorite':
        new_info = str(new_info).upper()[0]
    list[index][f"{info_check}"] = new_info
    colors(f"\n{str(info_check).upper()}'S contact updated!", 'YELLOW')
    return

def favorite_contact(list, index):
    if list[index]["favorite"] == 'Y': 
        list[index]["favorite"] = 'N'
        colors(f"{str(list[index]["name"]).upper()} is not a favorite contact anymore!",'MAGENTA')
    else:
        list[index]["favorite"] = 'Y'
        colors(f"{str(list[index]["name"]).upper()} is now a favorite contact!",'MAGENTA')
    return