import os

from user import User
from menu import Menu
from game import Game

if __name__ == "__main__":

    # provide permission tu use colour
    os.system("")

    user = User(input("--> username: "))

    choice = ""
    response = ""
    valid = False
    while choice.upper() != "QUIT":

        # avoids show the menu a few times when back to menu from somewhere in the game
        if not valid:
            Menu.show_menu(user.name)
            valid = False

        if response == "m":
            Menu.show_menu(user.name)
            choice = ""
            response = ""

        if choice.upper() == "STATICS":
            response = Menu.show_statics(user)
        elif choice.upper() == "RULES":
            response = Menu.show_rules(user)
        elif choice.upper() == "PLAY":
            response = Game.play_quiz_it(user)
        else:
            # provide a chance to write again if user write by mistake on the menu
            i = 0
            while choice.upper() not in ['STATICS', 'RULES', 'PLAY', 'QUIT']:
                choice = input("Please select one : " if not i else "Enter a valid choice : ")
                i = 1
            valid = True
