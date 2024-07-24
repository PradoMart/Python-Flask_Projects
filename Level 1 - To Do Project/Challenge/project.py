from models import*

contacts_list =[]

while True:
    menu()
    try:
        print()
        choice = int(input('\033[1mWhat do you like to do? \033[m'))
        print()
        
        if choice == 7:
            titles('The program has finished. see you!','YELLOW')
            break
        
        elif choice == 1:
            titles('ADDING CONTACT','GREEN')
            name = str(input("What's the contact's name? ").strip().title())
            phone = str(input("What about the phone: ").strip())
            email = str(input("And now the e-mail: ").strip())
            favorite = str(input("Would you like to favorite this contact?\nType only [YES] or [NO]: ").strip().upper())[0]
            while favorite not in 'YN':
                favorite = str(input("\033[1;33mSorry, option invalid!\033[m Try again [YES / NO]: ").strip().upper())[0]
            add_contact(contacts_list, name, phone, email, favorite)

        elif choice == 2:
            see_contacts(contacts_list, "CONTACT'S LIST", color='CYAN')

        elif choice == 3:
            see_contacts(contacts_list, 'EDTING CONTACT', color= 'YELLOW')
            index_contact = int(input('What contact do you wanna edit? ')) - 1 
            titles('NEW INFORMATIONS', color= 'YELLOW', tam= int(83))
            
            check_changes = str(input(f"Would you like to edit all {str(contacts_list[index_contact]["name"]).upper()}'S infos ? [YES / NO] ")).strip().upper()[0]
            while check_changes not in 'YN':
                check_changes = str(input(f"\033[1;33mSorry, option invalid!\033[m Try again [YES / NO]: ")).strip().upper()[0]

            if check_changes == 'N':
                print(f"Here's the informations you can edit:", end= ' ')
                for k, v in enumerate(contacts_list):
                    if k == 0:
                        print(f"\033[1m{v.keys()}\033[m")
                    pass
                
                variable_check = str(input("What info would you like to edit? ")).strip().lower()
                while variable_check not in v.keys():
                    variable_check = str(input("\033[1;33mSorry, option invalid!\033[m Try again [YES / NO]: ")).strip().lower()
                new_info = input("Write the new information: ").strip()
                edting_some_info(contacts_list, index_contact, variable_check, new_info)
            else:
                new_name = str(input("What's the contact's \033[1mNEW name\033[m? ").strip().title())
                new_phone = str(input("What about the \033[1mNEW phone\033[m: ").strip())
                new_email = str(input("And now, what's the \033[1mNEW e-mail\033[m: ").strip())
                new_favorite = str(input("Would you like to favorite this contact? Type only [YES] or [NO]: ").strip().upper())[0]
                edit_contacts(contacts_list, index_contact, new_name, new_phone, new_email, new_favorite)
            colors('-' * 83, 'YELLOW')
        
        elif choice == 4:
            see_contacts(contacts_list, 'FAVORITING A CONTACT', color= 'MAGENTA')
            index_contact = int(input('What contact do you wanna change the favorite status? ')) - 1
            favorite_contact(contacts_list, index_contact)

        elif choice == 5:
            see_contacts(contacts_list, "FAVORITE CONTACT'S LIST", True, 'MAGENTA')
        
        elif choice == 6:
            see_contacts(contacts_list, 'DELETING A CONTACT', color='RED')
            index_contact = int(input('What contact do you wanna delete? ')) - 1
            del contacts_list[index_contact]
            colors('Contact deleted!','RED')

    except Exception as problem:
        colors(f"Something went wrong! Here's the problem: {str(problem).upper()}",'YELLOW')