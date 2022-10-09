import inspect
from functools import wraps
from types import FunctionType
import re

CONTACTS: dict[str, dict[str, int]] = {}


def input_error(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        try:
            result = handler(*args, **kwargs)
        except KeyError as e:
            print(f'You entered a wrong name {e} that is not in the list. Please enter once again')
        except ValueError as e:
            print(e)
        except IndexError as e:
            print('You entered a wrong data. Please enter once again')
        else:
            return result

    return wrapper


@input_error
def hello_func():
    return 'How can I help you?'


@input_error
def exit_func():
    return 'Good bye!'


@input_error
def add_contact(name: str, phone: str) -> str:

    # if phone:
        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, phone)
        if not match:
            print("Invalid, please enter a valid phone number")
        #     print("Valid")
        # else:


        if CONTACTS.get(name):
            raise ValueError("Контакт було додано вже раніше \n"
                         "The contact details has already been added ")

        CONTACTS.update({name: {"name": name, "phone": phone}})

        return 'The contact details have been added.'

@input_error
def phone_сontact(name: str, phone: str) -> str:
    return CONTACTS[name]["phone"]

def validate_phone(phone: str):
    result = re.search(r"(^380|0|80)\d{9}$", CONTACTS[phone])

    if not result:
        raise ValueError(f'The phone number is invalid, {phone}.')


@input_error
def change_contact(name: str, old_phone: str, new_phone: str) -> str:

    if phone:
        pattern = r"(^380|0|80)\d{9}$"
        match = re.fullmatch(pattern, phone)
        if match:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

    CONTACTS[name]['phone'] = new_phone

    return f'The phone number for {name} was changed from {old_phone} to {new_phone}. ' \
           f'And it is updated in the main file.'


@input_error
def show_all() -> str:
    format_contacts = []

    for contact in CONTACTS.values():
        contact = f"{contact['name']}: {contact['phone']}"

        format_contacts.append(contact)

    return '\n'.join(format_contacts)


COMMANDS = {
    'hello': hello_func,
    ('exit', 'good bye', 'close'): exit_func,
    'add': add_contact,
    'phone': phone_сontact,
    'change': change_contact,
    'show all': show_all
}


@input_error
def search_args(data: str) -> tuple[FunctionType, list[str] | None]:
    for command, func in COMMANDS.items():

        if data.lower().startswith(command):
            args = data[len(command):].strip().split(' ')

            if check_args(func, args):
                return func, args

            return func, None
    else:
        raise ValueError("You entered an unknown command. Please enter the required command.\n")


def check_args(func, args: list) -> bool:
    func_params = inspect.getfullargspec(func.__dict__['__wrapped__']).args

    if not func_params:
        return False

    if len(func_params) == len(args):
        return True

    raise ValueError("Not all mandatory command arguments are listed\n")


def main():
    while True:
        data = input('\nEnter command: ')

        args = search_args(data)

        if args:
            handler = args[0]
            args = args[1]

            result = handler(*args) if args else handler()

            if result:
                print('\n' + result)

            if result == 'Good bye!':
                break


if __name__ == '__main__':
    main()
