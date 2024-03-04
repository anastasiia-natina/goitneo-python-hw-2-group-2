def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Give me name and phone please."
        
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def delete_contact(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    else:
        return "Contact not found."
