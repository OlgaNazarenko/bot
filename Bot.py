
CONTACTS: dict[str,int] = {}

def input_error(handler):
    def wrapper():
        try:
            result = handler()
        except KeyError as ke:
            print('You entered a wrong name that is not in the list. Please enter once again')
        except ValueError as ve:
            print('You provided an invalid value to a function. Please enter once again')
        except IndexError as ie:
            print('You entered a wrong data. Please enter once again')
    return wrapper

@input_error
def hello_func():
    print('How can I help you?')

@input_error
def exit_func():
    print('Good bye!')
    exit()

@input_error
def add_contact():
    name = input('Enter your name: ')
    phone = input('Enter your phone number:')
    CONTACTS[name] = phone
    print('The contact details have been added.')

@input_error
def change_contact():
    name = input('Enter your name: ')
    old_phone = input('Please enter your old phone, which you would like to change:')
    new_phone = input('Enter a new phone number:')
    CONTACTS[name][old_phone] = new_phone
    print(f'The phone number for {name} was changed from {old_phone} to {new_phone}. And it is updated in the main file.')

@input_error
def show_all():
    # print('\n'.join(f'{CONTACTS[name]}{CONTACTS[phone]}'))

    print('\n'.join([f'{phone}'for phone in CONTACTS.items()]))

COMMANDS = {
    'hello': hello_func,
    'exit': exit_func,
    'good bye': exit_func,
    'close': exit_func,
    'add': add_contact,
    'phone': add_contact,
    'change': change_contact,
    'show all': show_all
}
def main():
    while True:
        data: str = input('Enter command:')
        if data not in COMMANDS:
            print('You entered an unknown command. Please enter the required command.')
            continue
        COMMANDS[data]()



if __name__ == "__main__":
    main()