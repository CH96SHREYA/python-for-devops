
# String Method Practice Questions

# Capitalization
# Write a Python function that takes a string and returns it with the first character capitalized.
def capitilize_first(input):
    return input.capitalize()
# Counting Occurrences
# Create a function that counts how many times a specific character appears in a given string.
def count_specific(input, character):
    return input.lower().count(character.lower())
# String Splitting
# Write a program that splits a sentence into a list of words.
def split_sentence(input):
    words_list = input.split(" ")
    for word in words_list:
        print(word)
# Removing Whitespace
# Implement a function that removes leading and trailing whitespace from a string.
def remove_extra_spaces(input):
    return input.strip();

def normalize_spaces(input):
    # words = input.split();
    return " ".join(input.replace(" ",""));
# Checking String Content
# Create a function that checks if a string contains only alphabetic characters.
def check_only_alpha_numeric(input):
    return input.isalnum()
# Case Conversion
# Write a program that converts a string to lowercase and then to uppercase.
def convert_case(input):
    return input.swapcase()
# Finding Substrings
# Implement a function that finds the index of a substring within a larger string.
def find_substring(input,partialInput):
    # return input.find(partialInput);  
    try:  
        position = input.index(partialInput,11,15)
        return position
    except ValueError:
        return 0;
# String Replacement
# Create a program that replaces all occurrences of a word in a sentence with another word.
def replace_word(input,oldWord,newWord):
    return input.lower().replace(oldWord.lower(), newWord.lower())
# Checking String Endings
# Write a function that checks if a string ends with a specific substring.
def check_ends_with(input, substring):
    return input.lower().endswith(substring);
# String Centering
# Implement a function that centers a string within a given width, padding with spaces.


# print(capitilize_first("shreya"))
# print(count_specific("sssss","r"))
# split_sentence("I am an Indian")
# print(remove_extra_spaces("      I am      Shreya     !!!!   "))
#print(normalize_spaces("      I am      Shreya     !!!!   "))
# print(check_only_alpha_numeric(null))
# print(convert_case("AmY"))
# print(find_substring("ShreyaChaturvedi","Chat"))
# print(replace_word("A cat jumps on bus. Bus then stops. Which crashes the other bus","BUS","car"))
print(check_ends_with("ShreyaChaturvedi","vedis"))



# Understanding join method - Use to join elements of an iterables : separator.join(iterable)
# words =["Hello","World","!"]
# print(" ".join(words))