
CONTACTS: dict[str,int] = {}

def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
#             result = handler()
              return handler(*args, **kwargs)
        except KeyError as ke:
            print('You entered a wrong name that is not in the list. Please enter once again')
        except ValueError as ve:
            print('You provided an invalid value to a function. Please enter once again')
        except IndexError as ie:
            print('You entered a wrong data. Please enter once again')
    return wrapper 

@input_error
def hello_func():
   return 'How can I help you?'

@input_error
def exit_func():
    return 'Good bye!'
  

@input_error
def add_contact(*args, **kwargs):
    return f'The contact details {name} {phone} have been added.'

@input_error
def change_contact():
     return f'The {old_phone} was changed to {new_phone}.'\
     f'And it is updated in the main file.'

@input_error
def show_all():
    # print('\n'.join(f'{CONTACTS[name]}{CONTACTS[phone]}'))

    return '\n'.join([f'{phone}'for phone in CONTACTS.items()])

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
     
        command, *args = data.split()
        if command not in COMMANDS:
            return COMMANDS[command](args)


if __name__ == "__main__":
    main()
