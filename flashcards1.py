import shelve
import datetime
from datetime import timedelta, datetime

# Creates or alters a shelf file fcdata. I think it sets the output file to '[]'

def init():
    sure = input("Are you sure you want to recreate the shelf file (y/n)?  ")
    if sure.lower()[0] == 'y':
        shelfFile = shelve.open('fcdata')
        output = []
        shelfFile['output'] = output
        shelfFile.close()
        main()
    else:
        main()

def six():
    shelfFile = shelve.open('fcdata')
    output = shelfFile['output']
    print(output)
    for i in output:
        print(i)
# A method that adds words and definitions from 'Notes1.txt' to the shelfFile output list

def update():
    filename = '/Users/ericschlosser/Desktop/Notes/Notes1.txt'
    l = 0
    shelfFile = shelve.open('fcdata')
    output = shelfFile['output']
    with open(filename) as file_object:
        lines = file_object.readlines()

    # Creates list of values within each card.
    # list[0] = item
    # List[1] = definition
    # list[2] = datetime date // This is the date the card will next be used.
    # list[3] = Number of consecutive right answers
    # list[4] = binary state that shows if the card has been used today
    for line in lines:

        if line[0] == '!':
            l += 1
            card = line.split('-')
            card[0] = card[0][1:]
            card[1] = '-'.join(card[1:])
            card = card[:2]
            print(card[1])
            card.append(datetime.today())
            card.append(1)
            card.append(0)
            # NEEDS TO BE REWRITTEN: NOW, IF THE PROGRAM SENSES A DUPLICATE, IT SKIPS, IT DOES NOT REPLACE.
            # for item in output:
            #     if card[0] != item[0]:
            output.append(card)

    shelfFile['output'] = output
    print(len(output))
    for x in output:
        print(x)
    shelfFile.close()
    print('\n\nUpdate Sucessful.\n\n')
    print(str(l) + ' new cards added.')
    main()

# Prints a list of today's cards
def print_list():
    shelfFile = shelve.open('fcdata')
    print("\n\n\nLIST OF TODAY'S WORDS\n\n\n")
    row = "{:15}: {:60}"
    for card in shelfFile['output']:
        print(row.format(card[0], card[1]))
    shelfFile.close()
    main()

def fc():
    word_list_today = []
    shelfFile = shelve.open('fcdata')
    word_list = shelfFile['output']
    for card in word_list:
        card[4] = 0
    for word in word_list:
        if word[2] <= datetime.today():
            word_list_today.append(word)


    while len(word_list_today) > 0:
        print('\n\n' + word_list_today[0][0] + '\n\n')
        answer = input('Enter definition: ')
        print('\n\n' + word_list_today[0][1] + '\n\n')
        card = word_list.pop(0)
        correct = input(' Did you get the question right or wrong or have you mastered the concept (type r, w, m or q)? ')
        if correct[0].lower() == 'r':
            if card[4] == 0:
                card[4] += 1
                card[3] += 1
                card[2] = datetime.today() + timedelta(days = card[3])
            word_list_today.append(card)

        if correct[0].lower() == 'w':
            if card[4] == 0:
                card[4] += 1
                card[3] = 1

                card[2] = datetime.today() + timedelta(days = 1)
            word_list_today.append(card)
        if correct[0].lower() == 'm':
            if card[4] == 0:
                card[4] +=1
                card[3] +=1
                card[2] = datetime.today() + timedelta(days = card[3])
            word_list.append(card)
        if correct[0].lower() == 'q':
            break

    for i in word_list_today:
        word_list.append(i)

    for i in word_list:
        print(i[2])

    shelfFile['output'] = word_list
    shelfFile.close()
    cont = input('\n\nList Completed: Type "y" to return to the main menu.')
    if cont == 'y':
        main()
    else:
        pass

def main():
    print("\n\n\nFlashcards: Main Menu\n\n")
    print("Print list of today's flashcards: Press['1']\n")
    print("Run today's flashcards:           Press['2']\n")
    print("Scan notes for flashcards:        Press['3']\n")
    print("Manually enter flashcards:        Press['4']\n")
    print("Quit:                             Press['5']\n")
    menu_choice = input("> ")
    if menu_choice == '1':
        print_list()
    elif menu_choice == '2':
        fc()
    elif menu_choice == '3':
        update()
    elif menu_choice == '4':
        manual()
    elif menu_choice == '5':
        pass
    elif menu_choice == '6':
        six()
    elif menu_choice == '0':
        init()

main()
