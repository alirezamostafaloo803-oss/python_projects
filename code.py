#bank works project

import os

works = {
    'CREAT BANK ACCOUNT' : True,
    'TRANSFER' : True,
    'WITHDRAW': True
}

def clear_screen():
    os.system('cls'  if os.name == 'nt' else 'clear')

def check_user_amount():
    while True:
        user_amount = input('Enter your amount money to creat bank account:')
        if user_amount.isdigit():
            if int(user_amount) > 0:
                return user_amount
            else:
                print('input only should be number.')
           
        else:
            print('input only should be number.')

def check_user_name():
    while True:
        user_name = input('Enter your name:')
        if user_name.isalpha():
            return user_name
        else:
            print('name only should be a string.')

def check_user_last_name():
    while True:
        user_lastname = input('Enter your last name:')
        if user_lastname.isalpha():
            return user_lastname
        else:
            print('last name only should be a string.')

def check_national_code():
    while True:
        user_national_code = input('Enter your national code:')
        if user_national_code.isdigit() and len(user_national_code) == 10:
                return user_national_code
        else:
            print('national code only should be a number.')


    
   

def creat_bank_account():
    if works['CREAT BANK ACCOUNT'] : clear_screen()
    print('---CREAT BANK ACCOUNT---')
    name = check_user_name()
    last_name = check_user_last_name()
    amount = check_user_amount()
    national_code = check_national_code()
    print(f"\naccount was created succsessfuly.")
    print(f"{name} {last_name}'s account with national code: {national_code} and {amount} dollars was created.")




def check_name_to_transfer():
    while True:
        user_name_to_transfer = input('Enter name to transfer money:')
        if user_name_to_transfer.isalpha():
            return user_name_to_transfer
        else:
            print('name only should be a string.')

def check_amount_to_transfer():
    while True:
        user_amount_to_transfer = input('Enter amount to transfer:')
        if user_amount_to_transfer.isdigit():
            if int(user_amount_to_transfer) > 0:
                return user_amount_to_transfer
            else:
                print('amount only should be a number.')
        else:
            print('amount only should be a number.')



def transfer():
    if works['TRANSFER'] : clear_screen()
    print('---TRANSFER---')
    name_transfer = check_name_to_transfer()
    amount_transfer = check_amount_to_transfer()
    print(f"{amount_transfer} dollars was transfered to the {name_transfer}'s account.")




def check_amount_to_withdraw():
    while True:
        user_amount_to_withdraw = input('Enter amount to with draw:')
        if user_amount_to_withdraw.isdigit():
            if int(user_amount_to_withdraw) > 0:
                return user_amount_to_withdraw
            else:
                print('amount only should be a number.') 
        else:
            print('amount only should be a number.')


def withdraw():
    if works['WITHDRAW'] : clear_screen()
    amount = check_amount_to_withdraw()
    print(f"{amount} dollars withdrew from your account.")


def run_complete():
    print('---WELCOME TO MY BANK---')
    print('1.CREAT BANK ACCOUNT')
    print('2.TRANSFER')
    print('3.WITHDRAW')
    choice = input('Enter your choice (1 , 2 , 3):')
    clear_screen()
    if choice == '1':
        creat_bank_account()
    elif choice == '2':
        transfer()
    elif choice == '3':
        withdraw()
    else:
        print('NOTHING WAS DONE!')

run_complete()

def continue_works():
    continue_input = input('do you want to continue?')
    if continue_input == 'yes':
        clear_screen()
        return run_complete()
    elif continue_input == 'no':
        print('THANKS FOR CHOSSING US')

continue_works()
