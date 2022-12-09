# pylint: disable=missing-docstring

# Warning:
# - One line of code for each method
# - Just look in the doc for the right method of the String class!

def add_comma(a_string):
    #pass # TODO: return a copy of the string with every word separated by a comma
    # example: add_comma("John Peter Jude") => "John, Peter, Jude"
    return a_string.replace(" ", ", ")

def belongs_to(a_string, a_word):
    #pass # TODO: return true if a_string contains a_word
    # example: belongs_to("hey jude", "jude") => True
    if a_word in a_string:
        return True
    else:
        return False

def count_repetition(a_string, a_substring):
    #pass # TODO: return how many times a_substring occurs in a_string
    # example: count_repetition("000123000123", "0") => 6
    return a_string.count(a_substring)

def is_a_question(a_string):
    #pass # TODO: return true if a_string ends with a "?"
    # example: is_a_question("How are you?") => True
    if a_string[-1] == "?":
        return True
    else:
        return False

def remove_surrounding_whitespaces(a_string):
    #pass # TODO: return a copy of the string with leading and trailing whitespaces removed
    # example: delete_surrounding_whitespaces("  hey yo  ") => "hey yo"
    return a_string.strip().rstrip()

def replace(initial_string, old_letter, new_letter):
    #pass # TODO: return a copy of the string with the new letter replacing the old one
    # example: replace("casanova", "a", "o") => "cosonovo"
    return initial_string.replace(old_letter, new_letter)

def full_description_concatenation(first_name, last_name, age):
    #pass # TODO: return a sentence with the first_name and the last_name capitalized and the age
    # You should use concatenation
    # example: full_description_concatenation("john", "doe", 33) => "John Doe is 33"
    return first_name.capitalize()+ " " + last_name.capitalize() + " is " + str(age)

def full_description_formatting(first_name, last_name, age):
    #pass # TODO: return a sentence with the first_name and the last_name capitalized and the age
    # You should use formatting
    # example: full_description_formatting("john", "doe", 33) => "John Doe is 33"
    return f'{first_name.capitalize()} {last_name.capitalize()} is {age}'