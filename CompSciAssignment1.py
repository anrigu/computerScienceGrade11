# -----------------------------------------------------------------------------
# Name:        Assignment 1 (assignment1.py)
# Purpose:     Assignment 1

# Author:      Anri Gu
# Created:     10/29/2018
# Updated:     10/29/2018
# -----------------------------------------------------------------------------
import random
import operator


def convert_string_to_int_list(input_str):
    int_list = []
    str_list = input_str.split(" ")
    for s in str_list:
        int_list.append(int(s))
    return int_list


def alphabet_list():
    alpha_list = []
    for i in range(ord("A"), ord("Z") + 1):
        alpha_list.append(chr(i))
    return alpha_list


def word_count(sentence):
    word_list = sentence.split(" ")
    count = 0
    for i in range(0, len(word_list)):
        count += 1
    return count


def bubble_sort_ascending(list_unsorted):
    for i in range(0, len(list_unsorted)):
        for j in range(1, len(list_unsorted) - i):
            if list_unsorted[j - 1] > list_unsorted[j]:
                temp_num = list_unsorted[j]
                list_unsorted[j] = list_unsorted[j - 1]
                list_unsorted[j - 1] = temp_num
    return list_unsorted


def arithmetic(num1, num2, oper):
    if oper == "+":
        operation = operator.add
    elif oper == "-":
        operation = operator.sub
    elif oper == "*":
        operation = operator.mul
    elif oper == "/":
        operation = operator.truediv
    elif oper == "//":
        operation = operator.floordiv
    return operation(num1, num2)


def encoder(word_string, alpha_list, movement_amount):
    character_list = []
    word_string_capitalize = word_string.upper()
    for i in range(0, len(word_string_capitalize)):
        character_list.append(word_string_capitalize[i])
    encoded_string = ""
    for i in character_list:
        if ord("A") <= ord(i) <= ord("Z"):
            new_letter_index = (ord(i) - ord("A") + movement_amount) % 26
            encoded_string += alpha_list[new_letter_index]
        elif i == " ":
            encoded_string += " "
        else:
            encoded_string += i
    return encoded_string


def decoder(word_string, alpha_list, movement_amount):
    character_list = []
    word_string_capitalize = word_string.upper()
    for i in range(0, len(word_string_capitalize)):
        character_list.append(word_string_capitalize[i])
    decoded_string = ""
    for i in character_list:
        if ord(i) >= ord("A") and ord(i) <= ord("Z"):
            new_letter_index = (ord(i) - ord("A") - movement_amount) % 26
            decoded_string += alpha_list[new_letter_index]
        elif i == " ":
            decoded_string += " "
        else:
            decoded_string += i
    return decoded_string


def password_generator(password_length):
    new_password = ""
    for i in range(0, password_length):
        character_gen = chr(random.randint(ord("!"), ord("~")))
        new_password += character_gen
    return new_password


loop = True
while loop:
    user_decision = input('''Choose an option below:
1. Word Count 
2. Bubble Sort
3. Basic Arithmetic (Addition, Subtraction, Multiplication, or Division)
4. Secret Message Encoder
5. Secret Message Decoder
6. Password Generator
7. Exit''')
    valid_input = True
    if user_decision == "1":
        phrase = input("Input a string you would like word counted. (**Punctuation and numbers will be included**)")
        print(word_count(phrase))

    elif user_decision == "2":
        while valid_input:
            string_unsorted_int = input("Input list of integers that you would like sorted! "
                                        "Please separated the numbers with a space (e.g. 5 4 3 1)")
            try:
                list_ints = convert_string_to_int_list(string_unsorted_int)
                valid_input = False
            except ValueError:
                print("Please enter a list of integers separated with spaces!")
        sorted_int_list = bubble_sort_ascending(list_ints)
        for num in sorted_int_list:
            print(num, end=" ")
        print()

    elif user_decision == "3":
        while valid_input:
            equation = input("Write an equation you would like solved (Operators allowed: +, -, /, *)."
                             " Please format the equation with a space between the numbers and the operator "
                             "(e.g. 5 + 2)").split(" ")
            try:
                print(arithmetic(int(equation[0]), int(equation[2]), equation[1]))
                valid_input = False
            except ValueError:
                print("Please enter a valid format!")

    elif user_decision == "4":
        requested_encoded_string = input("Input a string you would like encoded!")
        while valid_input:
            shifted_letters = input("Input the number of letters you would like each letter to shift! (e.g. 3 would "
                                    "shift A to D and 1 to 4)")
            try:
                print(encoder(requested_encoded_string, alphabet_list(), int(shifted_letters)))
                valid_input = False
            except ValueError:
                print("Enter a valid shift amount!")

    elif user_decision == "5":
        requested_decoded_string = input("Input a string you would like decoded!")
        while valid_input:
            shifted_letters = input(
                "Input the number of letters you would like each letter to shift! (e.g. 3 would shift"
                " D to A and 4 to 1)")
            try:
                print(decoder(requested_decoded_string, alphabet_list(), int(shifted_letters)))
            except ValueError:
                print("Enter a valid shift amount!")

    elif user_decision == "6":
        while valid_input:
            length_password = input("How long would you like your password to be?")
            try:
                length_password_int = int(length_password)
                print(password_generator(length_password_int))
                valid_input = False
            except ValueError:
                print("Enter valid password length")

    elif user_decision == "7":
        print("Ok! Quit.")
        loop = False
    else:
        print("You didn't enter a number on the menu. Automatic quit.")
        loop = False
