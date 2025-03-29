"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marek Ječmínka
email: jecminkam@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

TEXT_0 = TEXTS[0].replace(".", "").replace("\n", "").replace(",", "").split(" ")
TEXT_1 = TEXTS[1].replace(".", "").replace("\n", "").replace(",", "").split(" ")
TEXT_2 = TEXTS[2].replace(".", "").replace("\n", "").replace(",", "").split(" ")
TEXTS_modified = [TEXT_0, TEXT_1, TEXT_2]

registered = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

user_name = input("Please enter your username: ")
user_password = input("Please enter your password: ")

if user_name not in list(registered):
    print("username:" + user_name)
    print("password:" + user_password)
    print("unregistered user, terminating the program...")
    quit()

elif registered[user_name] == user_password:
    print("\nusername:" + user_name +
          "\npassword:" + user_password)
    print(40 * "-")
    print("Welcome to the app,", user_name,
          "\nWe have 3 texts to be analyzed.")
    print(40 * "-")
    selection = input("Enter a number btw. 1 and 3 to select: ")

    if not selection.isdigit():
        print("Yous selection is not digit. Please enter digit next time!")
        quit()

    elif selection not in ("1", "2", "3"):
        print("Your selection is not in range. Please enter a number btw. 1 and 3 next time!")
        quit()
    
    words = []
    title_words = []
    upper_words = []
    lower_words = []
    numbers = []

    for word in TEXTS_modified[int(selection) - 1]:
        if word != "":
            words.append(word) 
        
    for word in TEXTS_modified[int(selection) - 1]:
        if word.istitle():
            title_words.append(word)
        elif word.isupper():
            upper_words.append(word)
        elif word.islower():
            lower_words.append(word)
        elif word.isdigit():
            numbers.append(int(word))
    
    print(40 * "-")
    print("There are", len(words), "words in the selected text.")
    print("There are", len(title_words), "titlecase words.")
    print("There are", len(upper_words), "uppercase words.")
    print("There are", len(lower_words), "lowercase words.")
    print("There are", len(numbers), "numeric strings")
    print("The sum of all the numbers", sum(numbers))
    print(40 * "-")

    words_length = []
    
    for word in words:
        words_length.append(len(word))

    for number in range(1, max(words_length) + 1):
        if number < 10:
            print(" " + str(number) + "|" + words_length.count(number) * "*" + (21 - words_length.count(number)) * " " + "|" + str(words_length.count(number)))
        else:
            print(str(number) + "|" + words_length.count(number) * "*" + (21 - words_length.count(number)) * " " + "|" + str(words_length.count(number)))

