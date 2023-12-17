# Chatbot EFREI L1
# William ROBERT | Batur HAMZAOGULLARI

from extract_files import *
import text_treatment
import tf_idf_related
import additional_functionalities

# -----------------------------------------------Programme Principale--------------------------------------------------#

path = "./speeches/"
path_cleaned = "./cleaned/"
list_file_names = list_of_files(path, "txt")
text_treatment.cleaned_speech(list_file_names)
while True:
    print("--Press a number to select a command--")
    print("-0- Exit")
    print("-1- Chatbot")
    print("-2- specific")

    main_command = input()

    if main_command == "0":
        break
    elif main_command == "1":
        print("nothing yet")
    elif main_command == "2":
        while True:
            print("--Press a number to select a command--")
            print("-0- Exit")
            print("-1- Print the least important words in the corpus")
            print("-2- Print the words with the highest TF-IDF score")
            print("-3- Print the most repeated words by president Chirac")
            print("-4- Print the presidents who talked about \"Nation\" and the one who repeated it the most")
            print("-5- Print the first president who talked about climate and/or ecology")
            print("-6- Print the words that all presidents mentioned apart from the \"unimportant words\"")
            print("-7- For any extra functionalities tailored to you")
            command = input()

            if command == "0":
                break
            elif command == "1":
                additional_functionalities.request_redundant_words(path_cleaned, 0)
                print()
            elif command == "2":
                additional_functionalities.request_highest_tf_idf(path_cleaned)
                print()
            elif command == "3":
                additional_functionalities.request_most_repeated_word(path_cleaned, "Chirac")
                print()
            elif command == "4":
                additional_functionalities.request_highest_said("nation")
                print()
            elif command == "5":
                additional_functionalities.request_word_search(path_cleaned, "climat")
                additional_functionalities.request_word_search(path_cleaned, "écologie")

                print()
            elif command == "6":
                additional_functionalities.request_common_words()
                print()
            elif command == "7":
                while True:
                    print("--Press a number to select a command--")
                    print("-0- Return to the previous menu")
                    print("-1- Select a number and any number that has an importance below it will be shown")
                    print("-2- Select a president to find out which word he said the most often")
                    print("-3- Select a word and find out which presidents mentioned it")
                    print("-4- Prints the most important word of every text")

                    sub_command = input()
                    if sub_command == "0":
                        break
                    elif sub_command == "1":
                        lvl = float(input("Enter a number: "))
                        additional_functionalities.request_redundant_words(path_cleaned, lvl)
                        print()
                    elif sub_command == "2":
                        print(text_treatment.president_last_name(list_file_names))
                        pres = input("Select any of the following presidents: ")
                        additional_functionalities.request_most_repeated_word(path_cleaned, pres)
                        print()
                    elif sub_command == "3":
                        wor = input("Enter a word: ")
                        additional_functionalities.request_highest_said(wor)
                        print()
                    elif sub_command == "4":
                        additional_functionalities.request_highest_tf_idf_file(path_cleaned)
                        print()
                    else:
                        print("Invalid command")
                        print()
            else:
                print("Invalid command")
                print()
    else:
        print("Invalid command")
        print()

