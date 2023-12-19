"""                                         Nom du projet : Chatbot EFREI L1
                                     Auteurs : William ROBERT | Batur HAMZAOGULLARI

This is the main file where everything converges, only the menu is here, everything else is imported from the other
files, rendering everything much easier to understand and trace back.
"""
import extract_files
# ______________________________________________Functions from part 2__________________________________________________#

from extract_files import *
import text_treatment
import additional_functionalities
import tf_idf_related
import Question_Answer

path = "./speeches/"
path_cleaned = "./cleaned/"

text_treatment.cleaned_speech(list_of_all_file_names)

print("Welcome to our Chatbot project! \n")
helper = ("First of all, you have 3 main choices at the beginning: \n "
        "- Firstly there is the \"functionalities\" section of the chatbot, which will allow you to select "
        "a number of \n  different options in order to extract the information you want out of the texts."
        "\n - Next up is the true \"Chatbot\" aspect of this program. You can enter any question you like "
        "and you'll get \n  a reasonably coherent answer. Please be polite and ask questions about the "
        "theme. \nIf at any time you wish to leave, please enter \"Exit\" and if you ever want to \nsee "
        "this guide again, enter \"/help\".")
while True:
    try:
        guide = input("Before we begin, would you like to take a quick guide on how to use this chatbot? Enter 'Yes' "
                      "if you do or 'No' if you don't: ")

        if guide.lower() == 'yes' or guide.lower() == "y":
            print("\nGreat! Let me provide you with a quick guide.\n")
            print(helper)
            break
        elif guide.lower() == 'no' or guide.lower() == "n":
            print("No problem! Let's proceed without a guide.")

            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    except Exception as malfunction:  # Malfunction is the error message
        print(f"Error: {malfunction}")

print(" \n|============================ Have a great time ! ============================|\n")

global_command_status = True

while global_command_status:
    print("Please enter any of the following options, if at any point you wish to leave, enter \"Exit\".\n"
          "If you wish to see the guide, enter \"/help\".")
    print("1. Launch the standalone functionalities")
    print("2. Launch the Chatbot")
    print("\n\"Exit\". Leave the Chatbot")
    global_command = input().lower()

    if global_command == "exit" or global_command == "0":
        global_command_status = False
        print("Thanks for stopping by, we hope you enjoyed yourself!")

    elif global_command == "/help" or global_command == "/h":
        print(helper)

    elif global_command == "1":

        while True:
            print("1. See the least important words in the corpus:")
            print("2. See the most important words in the corpus of documents:")
            print("3. See the most repeated words by president Chirac")
            print("4. See the presidents who talked about \"Nation\" and the one who repeated it the most")
            print("5. Learn who was the first president to talk about climate and/or ecology")
            print("6. For any extra functionalities tailored to you")
            print("\"Back\" Return to main menu")
            sub_command = input().lower()

            if sub_command == "back" or sub_command == "b":
                break

            elif sub_command == "exit":
                global_command_status = False
                print("Thanks for stopping by, we hope you enjoyed yourself!")
                break

            elif sub_command == "/help":
                print("\n", helper, "\n")

            elif sub_command == "1":
                additional_functionalities.request_redundant_words(0.0, list_of_all_file_names)

                print()

            elif sub_command == "2":
                additional_functionalities.request_highest_tf_idf(list_of_all_file_names)
                print()

            elif sub_command == "3":
                additional_functionalities.request_most_repeated_word("Chirac", list_of_all_file_names)
                print()

            elif sub_command == "4":
                additional_functionalities.request_highest_said("nation", list_of_all_file_names)
                print()

            elif sub_command == "5":
                additional_functionalities.request_word_search("climat", list_of_all_file_names)
                additional_functionalities.request_word_search("écologie", list_of_all_file_names)
                print()

            elif sub_command == "6":

                while True:
                    print("1. Select a number and any number that has an importance below it will be shown")
                    print("2. Select a president to find out which word he said the most often")
                    print("3. Select a word and find out which presidents mentioned it")
                    print("4. Prints the most important word of every text")
                    print("5. Show the words that all presidents mentioned apart from the \"unimportant words\"")
                    print("\n\"Back\" Return to the previous menu")
                    inner_command = input().lower()

                    if inner_command == "back" or inner_command == "b":
                        break
                    elif inner_command == "exit" or global_command == "0":
                        global_command_status = False
                        print("Thanks for stopping by, we hope you enjoyed yourself!")
                        break

                    elif inner_command == "/help":
                        print("\n", helper, "\n")

                    elif inner_command == "1":
                        lvl = float(input("Enter a number: "))
                        additional_functionalities.request_redundant_words(lvl, list_of_all_file_names)
                        print()

                    elif inner_command == "2":
                        # The user could indeed enter something unexpected and cause the program to crash
                        print(text_treatment.president_last_name(list_of_all_file_names))
                        pres = input("Select any of the following presidents: ")
                        additional_functionalities.request_most_repeated_word(pres, list_of_all_file_names)
                        print()

                    elif inner_command == "3":
                        # Same thing for this command
                        wor = input("Enter a word: ")
                        additional_functionalities.request_highest_said(wor, list_of_all_file_names)
                        print()

                    elif inner_command == "4":
                        additional_functionalities.request_highest_tf_idf_file()
                        print()

                    elif inner_command == "5":
                        additional_functionalities.request_common_words(list_of_all_file_names,
                                                                        text_treatment.president_last_name(
                                                                            list_of_all_file_names))
                        print()
                    else:
                        print("Invalid command")
                        print()

            else:
                print("Invalid command")
                print()

    elif global_command == "2":
        print("Welcome to the custom question area! \n Please make sure that your question doesn't have any typos in "
              "order to maintain optimal performances. \n If you spot any errors or inconsistencies please inform "
              "one of the main contributors.")

        user_question = input("Please enter your question: ")
        while True:  # Just to make sure that the question is valid
            found = False
            for word in text_treatment.cleaned_text(user_question).split():  # checking to see if there are words from
                # the question in any of the texts
                if word in tf_idf_related.list_words(path_cleaned):
                    found = True
                    break

            if found:
                break
            print("This question cannot be be answered with our current documents.")
            user_question = input("Please enter your question: ")

        entered_question = Question_Answer.tokenise_question(user_question) # Tokenise the question to use it afterward
        question_document_common_words = Question_Answer.search_related_words(entered_question) # Search for words in
        # the question that are also in the corpus of documents
        question_TF_score = Question_Answer.question_TF(question_document_common_words) # Calculate the TF score for the
        # question
        question_TF_IDF_score = Question_Answer.question_TF_IDF(question_TF_score) # Based off of the question's TF
        # Score, it determines the question's TF-IDF score alongside the corpus of documents
        question_TF_IDF_score_conversion = Question_Answer.TF_IDF_conversion(question_TF_IDF_score) # Turn it into a
        # 2D array
        question_most_important_word = Question_Answer.highest_tf_idf(question_TF_IDF_score)
        question_important_word_in_files = Question_Answer.files_with_important_word(question_most_important_word,
                                                                                     extract_files.list_of_all_file_names)
        #
        question_most_similar_document = Question_Answer.most_relevant_document(question_TF_IDF_score_conversion,
                                                                                Question_Answer.score_TF_IDF_Array,
                                                                                question_important_word_in_files)

        final_answer = Question_Answer.response_generation(question_most_similar_document, question_most_important_word,
                                                           user_question)
        print(final_answer)
