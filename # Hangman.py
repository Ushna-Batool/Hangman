import random, time, sys

# global variables
max_errors = 3
number_of_attempts = 0  # added this to fix a bug
guessed = []  # list of guessed words
list_of_letters = 'First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth'.split()  # needed for print
master_dict = {'Cities Of Pakistan': 'Multan Karachi Islamabad Rawalpindi Hyderabad '.split(),  # dictionary of words
               'Flavours of Ice-cream': 'Vanilla chocolate strawberry berry'.split(),
               'Objects': 'table chair bag book dustbin door'.split()
               }
hangman_stages = ['''
   +---+
       |
       |
       |
      === ''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
# pictionary of hangman (minimised)


def choose_a_word(dictionary):
    master_dict = dictionary
    for k in master_dict:  # capitalise every value in dictionary
        for i in range(len(master_dict[k])):  # capitalise all list
            master_dict[k][i] = master_dict[k][i].upper()

    # to choose a random key(category) and value(word within that category)
    global word_key_value
    word_key_value = random.choice(list(master_dict.keys()))
    word_index_value = random.randint(0, len(master_dict[word_key_value]) - 1)
    return master_dict[word_key_value][word_index_value]


def slow_print(t):
    for i in t:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0)  # change later #
    print('')


def list_to_string(s):  # helper function( just hide )
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def initialise(w):  # a welcome script. Ignore

    slow_print('Welcome to Hangman! \nYou have 7 available lives by default.')
    print('Your word has', len(w), 'letters\n Your word is in the category:', word_key_value)
    print('_' * len(w))


def difficulty():
    while True:
        ask = input('Do you want to choose a difficulty level? [y/n]:')
        if len(ask) == 1 and ask.isalpha() is True:  # checking input
            ask = ask.lower()
            if ask == 'y':
                for i in range(max_errors + 1):
                    hangman_difficulty = input('Choose your difficulty: Easy[ 1 ], Medium[ 2 ] or Hard [ 3 ]: ')
                    if len(hangman_difficulty) == 1 and hangman_difficulty.isnumeric() is True:
                        if hangman_difficulty == '1':
                            return 7
                        elif hangman_difficulty == '2':
                            return 5
                        elif hangman_difficulty == '3':
                            return 3
                    else:
                        print('Input Error. Enter a Valid Value.')

            elif ask == 'n':
                return 7

        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be either Y or N ')


def main_program(user_tries, word,  difficulty_level):
    error_counter = 0
    counter_for_letter = 0
    try:
        max_tries = difficulty_level

    except TypeError:
        print('Input Error. Enter a Valid Value.'
              '\nValue has to be either Y or N ')

    while user_tries <= max_tries - 1:
        user_try = input('Try to guess your ' + str(list_of_letters[counter_for_letter]) + ' letter: ')


        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try in word:  # if guess is correct
                print('You are Correct!')
                counter_for_letter += 1
                func_word = word  # made for use in the for loop below (can be ignored)

                for u in range(len(word)):
                    if func_word.find(user_try) == -1:  # check if char is not in word
                        break
                    else:
                        chars_in_word.pop(func_word.find(user_try))  # remove char from list
                        chars_in_word.insert(func_word.find(user_try.upper()), user_try)  # add user_try to list
                        func_word = func_word.replace(user_try, str(u), 1)  # modify func_word
                print(list_to_string(chars_in_word))  # print letters user got right

                if word == list_to_string(chars_in_word):  # if user wins. print win statement
                    print('You won!. Congratulations!!!!')
                    break

            elif user_try not in word:  # if guess is incorrect
                if user_try in guessed:
                    print('You have already guessed this!\nTry again.')

                else:
                    if user_tries < max_tries - 1:
                        print('Your guess is incorrect.\n Try Again')
                        print(hangman_stages[user_tries])
                    else:
                        print('You have used up all your tries, sorry.'
                              '\nGame Lost!')
                        print(hangman_stages[user_tries])
                    guessed.append(user_try)  # make a list of words user has guessed
                    user_tries += 1

        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be a single character from the English Alphabet')
            error_counter += 1
            if error_counter > max_errors:
                print('Too many Input Errors!. Game over')
                break


generated_word = choose_a_word(master_dict)
chars_in_word = ['_'] * (len(generated_word))  # used to display the words user got right
initialise(generated_word)  # program starts
main_program(number_of_attempts, generated_word, difficulty())  # while loop
