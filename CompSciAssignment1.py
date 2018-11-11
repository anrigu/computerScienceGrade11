# -----------------------------------------------------------------------------
# Name:        Assignment 1 (assignment1.py)
# Purpose:     Assignment 1

# Author:      Anri Gu
# Created:     10/29/2018
# Updated:     11/5/2018
# -----------------------------------------------------------------------------
import random
import operator


def convert_string_to_int_list(input_str):
    '''
    This function changes a string of integers into a list of integers

    This function will split the input string and convert each integer from the string to an integer

    Parameters
    ----------
    input_str : string

    Returns
    -------
    list
      List of the integers passed in from the input string
    '''
    int_list = []
    str_list = input_str.split(" ")
    for s in str_list:
        int_list.append(int(s))
    return int_list


def alphabet_list():
    '''
    This function creates a list of all the capital case letters in the alphabet

    This function will be used as the alpha_list parameter in the encoder and decoder. It will add all the letters into a list which will be returned.

    Parameters
    ----------
    None

    Returns
    -------
    list
      A list of the capital letters of the alphabet
    '''
    alpha_list = []
    for i in range(ord("A"), ord("Z") + 1):
        alpha_list.append(chr(i))
    return alpha_list


def word_count(sentence):
    '''
    This function is used to count the words of the input string

    After inputting a string, it loops through the split version of the input. It will add 1 to count everytime it loops through until it reaches the length of the string.

    Parameters
    ----------
    sentence : str
      A string of words user would like word counted

    Returns
    -------
    int
      Number of words in their input string
    '''
    return len(sentence.split())


def binary_search(num_to_find, sorted_num_list):
    '''
    This function is used to search through a list to check if a number is located in it

    It binary searches through the input list to see if the input number is located in it. If the number is not in the list, the function will return -1

    Parameters
    ----------
    num_to_find : int
      the number that is trying to be found
    sorted_num_list : list
      a sorted list of numbers in ascending order

    Returns
    -------
    int
      the index of the number that is trying to be found within the input list of integers. If not found, the return is -1
    '''
    lower_index = 0
    upper_index = len(sorted_num_list) - 1
    while lower_index <= upper_index:
        middle_index = (upper_index - lower_index) // 2 + lower_index
        if sorted_num_list[middle_index] == num_to_find:
            return middle_index
        elif sorted_num_list[middle_index] < num_to_find:
            lower_index = middle_index + 1
        else:
            upper_index = middle_index - 1
    return -1


def arithmetic(num1, num2, oper):
    '''
    This function solves a simple arithmetic equation.

    It will evaluate the operator and check what operator(e.g. addition, subtraction, multiplication or division) has been passed in.
    It will then correspond it to the correct operator and then complete the equation.

    Parameters
    ----------
    num1 : int
      The first integer value in the equation
    num2 : int
      The second integer value in the equation
    oper : str
      The operator in the equation

    Returns
    -------
    int
      The answer to the equation
    '''
    if oper == "+":
        operation = operator.add
    elif oper == "-":
        operation = operator.sub
    elif oper == "*":
        operation = operator.mul
    elif oper == "/":
        operation = operator.floordiv
    return operation(num1, num2)


def encoder_decoder(word_string, alpha_list, movement_amount):
    '''
    This function shifts each letter in a string by the movement amount.

    If the passed in movement amount is positive, it will shift all the letters right (e.g. A --> D). This is the encoder formula.
    If the passed in movement amount is negative, it will shift all the letters left (e.g. D --> A). This is the decoder formula.

    Parameters
    ----------
    word_string : str
      a string that user wants to have encoded/decoded
    alpha_list : list
      a list of the capital letters in the alphabet
    movement_amount : int
      the number of letters the user wants to shift each letter

    Returns
    -------
    str
      string of the encoded/decoded inputted string
    '''
    encoded_string = ""
    for letter in word_string:
        upper_letter = letter.upper()
        if ord("A") <= ord(upper_letter) <= ord("Z"):
            new_letter_index = (ord(upper_letter) - ord("A") + movement_amount) % 26
            encoded_string += alpha_list[new_letter_index]
        elif letter == " ":
            encoded_string += " "
        else:
            encoded_string += letter
    return encoded_string


def password_generator(password_length):
    '''
    This function is used to generate a password.

    The password is as long as the inputted password_length. The characters that are allowed in the password are between the ASCII values of 33 and 126, inclusive

    Parameters
    ----------
    password_length : int
      the length of the desired password

    Returns
    -------
    str
      the generated password
    '''
    new_password = ""
    if password_length >= 0:
        for i in range(0, password_length):
            character_gen = chr(random.randint(ord("!"), ord("~")))
            new_password += character_gen
    else:
        new_password += "Enter a valid length for the password!"
    return new_password


# assert (convert_string_to_int_list("1 2 3 4 5") == [1, 2, 3, 4, 5]),"Expect the string of integers to return a list of the same integers  "
# assert (alphabet_list() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']),"Expect a return of the capital letters of the alphabet"
# assert (word_count("Hi my name is Assignment1") == 5), "Expect a return of 5 as the word count"
# assert (binary_search(2,[1,2,3,4]) == 1), "Expect a return of 1 as the index of the number 2 in the given list"
# assert (arithmetic(1,2,"+") == 3), "Expect a return of 3 as the inputted numbers 1 and 2 should add to give 3"
# assert (encoder_decoder("Hi my name is Anri", alphabet_list(), 3) == "KL PB QDPH LV DQUL"), "Expecting the cipher to encode the input to Kl pb qdph lv Dqul"
# assert (encoder_decoder("KL PB QDPH LV DQUL",alphabet_list(),-3)) == "HI MY NAME IS ANRI", "Expecting the cipher to decode the input "
# assert (len(password_generator(10)) == 10), "Expect the length of the password to be 10"


loop = True
while loop:
    user_decision = input('''Choose an option below:
1. Word Count 
2. Binary Search
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
        number_list = [1, 2, 3, 4, 5, 7, 8, 9, 12, 23, 45, 50, 65, 72, 76, 82, 94, 105]
        while valid_input:
            string_unsorted_int = input("Input a number you would like found in a list of numbers ")
            try:
                print(binary_search(int(string_unsorted_int), number_list))
                valid_input = False
            except ValueError:
                print("Please enter an integer!")

    elif user_decision == "3":
        while valid_input:
            equation = input("Write an equation you would like solved (Operators allowed: +, -, /, *)."
                             " Please format the equation with a space between the numbers and the operator "
                             "(e.g. 5 + 2)").split(" ")
            try:
                print(arithmetic(int(equation[0]), int(equation[2]), equation[1]))
                valid_input = False
            except:
                print("Please enter a valid format!")

    elif user_decision == "4":
        requested_encoded_string = input("Input a string you would like encoded!")
        while valid_input:
            shifted_letters = input("Input the number of letters you would like each letter to shift! (e.g. 3 would "
                                    "shift A to D and 1 to 4)")
            try:
                print(encoder_decoder(requested_encoded_string, alphabet_list(), int(shifted_letters)))
                valid_input = False
            except ValueError:
                print("Enter a valid shift amount!")

    elif user_decision == "5":
        requested_decoded_string = input("Input a string you would like decoded!")
        while valid_input:
            shifted_letters = input(
                "Input the number of letters you would like each letter to shift! (e.g. 3 would shift"
                " D to A and 4 to 1)")
            valid_input = False
            try:
                print(encoder_decoder(requested_decoded_string, alphabet_list(), -(int(shifted_letters))))
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
