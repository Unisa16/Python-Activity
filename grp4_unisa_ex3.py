# Program to calculate the length of a string
def calculate_length(string):
    return len(string)

# Program to count the number of characters in a string
def count_characters(string):
    return len(string)

# Program to replace occurrences of first character with '$', except the first char itself
def replace_first_char(string):
    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')
    return modified_string

# Program to swap the first two characters of two strings and concatenate them
def swap_and_concatenate(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + ' ' + new_str2

# Program to concatenate four variables using + and space
def concatenate_four_strings(var1, var2, var3, var4):
    return var1 + " " + var2 + " " + var3 + " " + var4

# Program to concatenate two user input strings
def concatenate_user_strings():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return str1 + " " + str2

# Program to concatenate your name and age in a paragraph
def concatenate_name_age(name, age):
    return "My name is " + name + " and I am " + age + " years old."

# Example usage
if __name__ == "__main__":
    # 1. Calculate the length of a string
    string = "Rafael Unisa"
    print(f"Length of the string: {calculate_length(string)}")
    
    # 2. Count the number of characters in a string
    print(f"Number of characters: {count_characters(string)}")

    # 3. Replace occurrences of first char with '$', except the first char
    modified_string = replace_first_char("restart")
    print(f"Modified string: {modified_string}")
    
    # 4. Swap first two characters of two strings and concatenate them
    concatenated_string = swap_and_concatenate("rafael", "cy")
    print(f"Swapped and concatenated string: {concatenated_string}")

    # 5. Concatenate four variables using + and space
    concatenated_four = concatenate_four_strings("Hello", "my", "name is", "ravine")
    print(f"Concatenated four strings: {concatenated_four}")

    # 6. Concatenate two user input strings
    user_concatenated = concatenate_user_strings()
    print(f"User concatenated string: {user_concatenated}")

    # 7. Concatenate name and age in a paragraph
    name = "Rafael"
    age = "21"
    paragraph = concatenate_name_age(name, age)
    print(paragraph)
