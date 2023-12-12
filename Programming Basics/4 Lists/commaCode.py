# This is Comma Code Project

def comma_code(list):
    if not list:  # Check for an empty list
        return "The list is empty"
    elif len(list) == 1:  # Check if there's only one item in the list
        return list[0]
    else:
        formatted_string = ', '.join(list[:-1]) + ', and ' + list[-1]
        return formatted_string

# Take user input as a string and convert it to a list by splitting on spaces
user_input = input("Enter items separated by spaces: ")
my_list = user_input.split()

result = comma_code(my_list)
print(result)
