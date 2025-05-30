"""
Write a search and replace program in Python.
This should first take the original text as input by prompting the user for it.
It should then, prompt the user for which word to search,
and what new word it should be replaced with.
"""

# URL = input("http://www.w3.org/1999/xhtml")
# print("Entered URL is: ", URL)
# for i in URL:
#     if i == "XHTML namespace":
#         print(i)
# say_something = input("Enter anything you want: ")
# def search_word():
#     word = input("Enter the word you want to search: ")
#     for word in say_something:
#         word.find(" ")
#         if word in say_something:
#             word.replace(" ","me")
#             print(word)
#
# search_word()

def search_and_replace():
    # Take the original text input from the user
    original_text = input("Enter the original text: ")

    # Prompt for the word to search
    search_word = input("Enter the word to search for: ")

    # Prompt for the new word to replace with
    replace_word = input("Enter the new word to replace with: ")

    # Replace the occurrences of the search word with the new word
    updated_text = original_text.replace(search_word, replace_word)

    # Display the updated text
    print("\nUpdated text:")
    print(updated_text)

# Run the program
if __name__ == "__main__":
    search_and_replace()


