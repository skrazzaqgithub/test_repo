# name=str(input("Enter your name:"))
# # surname=str(input("Enter your surname:"))
# # print(name)
# # print("Name:", name, "Surname:", surname)
# # surname=surname[-5]
# # name=name[-1]
# # print(name)
# # name1=str(input("Enter your name:"))
# # name1=name1[-5:]
# # print(name1)
# name=name[2:6:3]
# print(name)


# n1=name.upper()
# n2=surname.upper()
# print(n1, n2)
# print("-------", "-----")
# n3 = n1.capitalize()
# n4 = n2.capitalize()
# print(n4, ",", n3)
# n4 = n4[2:4]
# print(n4)

# Prompting the user to enter a long sentence
sentence = input("Enter a long sentence: ")

# Finding the last character in the sentence
last_character = sentence[-1]

# Finding the last 5 characters in the sentence
last_five_characters = sentence[-5:]

# Printing the characters at the 2nd and 5th positions (indexing starts at 0)
second_and_fifth_characters = sentence[1] + sentence[4]

# Finding the character at the center of the string and the two adjoining characters
length = len(sentence)
center_index = length // 2
center_and_adjacent = sentence[center_index - 1:center_index + 2]

# Outputting the results
print(f"Last character in the sentence: {last_character}")
print(f"Last 5 characters in the sentence: {last_five_characters}")
print(f"Characters at 2nd and 5th positions: {second_and_fifth_characters}")
print(f"Center character with its adjoining characters: {center_and_adjacent}")