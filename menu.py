import plotext as plt
import time
from colorama import Fore


class Menu:

    # to fit the titles depends on length of user's name
    @staticmethod
    def fitting(space, string):
        if (space - len(string)) % 2 == 0:
            one_side = (space - len(string)) / 2
        else:
            one_side = (space - len(string)) // 2
        return int(one_side)

    @staticmethod
    def show_menu(user):
        name = user.upper()
        len_name = len(name)
        space = 40 + len_name
        print(" " * 15 + f" {Fore.LIGHTCYAN_EX} HELLO {name} !!! {Fore.RESET}" + " " * 15)
        one_side = 0

        one_side = Menu.fitting(space, "WELCOME TO QUIZIT")

        print(" " * int(one_side) + Fore.LIGHTCYAN_EX + "WELCOME TO QUIZIT" + Fore.RESET + " " * (space - int(one_side)))

        one_side = Menu.fitting(space, "LET'S ENJOY AND LEARN")

        print(" " * int(one_side) + Fore.LIGHTCYAN_EX + "LET'S ENJOY AND LEARN" + " " * (space - int(one_side)) + Fore.RESET)

        one_side = Menu.fitting(space, "   RULES   ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + ">" + Fore.RESET + Fore.LIGHTWHITE_EX + "   RULES   " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * (space - 12 - int(one_side)) + Fore.RESET)

        one_side = Menu.fitting(space, "   PLAY   ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + ">" + Fore.RESET + Fore.LIGHTWHITE_EX + "   PLAY   " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * (space - 11 - int(one_side)) + Fore.RESET )

        one_side = Menu.fitting(space, "   STATICS   ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + ">" + Fore.RESET + Fore.LIGHTWHITE_EX + "  STATICS   " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * (space - 14 - int(one_side)) + Fore.RESET)

        one_side = Menu.fitting(space, "   QUIT   ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + ">" + Fore.RESET + Fore.LIGHTWHITE_EX + "   QUIT   " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * (space - 11 - int(one_side)) + Fore.RESET )

    # the method is for second of statics
    @staticmethod
    def statics_2(type_lst, type_for_show):
        # controls if the user play the quiz of the category
        # finds the highest score
        if type_lst:
            # firstly, assigns the first score
            high_score = float(type_lst[0][3])
            # looks whether there is higher score or not
            for lst in type_lst:
                if float(lst[3]) >= high_score:
                    high_score = float(lst[3])

            # if user play the quiz less than 3 times, the graph show how many scores there are
            if len(type_for_show) < 3:
                categories = [f"Last {i + 1}" for i in range(len(type_for_show))]
                categories.append("highest score")
                percentages = [type_for_show[i] for i in range(len(type_for_show))]
                percentages.append(high_score)
            else:
                categories = ["Last 3", "Last 2", "Last 1", "highest score"]
                percentages = [type_for_show[0], type_for_show[1],
                               type_for_show[2], high_score]

            Menu.graph_plot(categories, percentages)
            print()
            input("Please, enter to back menu")
            print()
            return "m"

        else:
            print()
            print("COME HERE AFTER PLAY GAME")
            input("Please, enter to back menu")
            print()
            return "m"

    # for graphics
    @staticmethod
    def graph_plot(categories, percentages):
        # to clear previous information used
        plt.clear_figure()
        plt.bar(categories, percentages, orientation="v", width=0.1, marker='fhd')
        plt.title("General Score Graph")
        plt.clc()  # to remove colors
        plt.plotsize(100,
                     (3 * len(
                         categories) - 1) + 9)
        plt.show()

    @staticmethod
    def show_statics(user):
        name = user.name
        space = 40 + len(name)
        print()

        one_side = Menu.fitting(space, "  STATICS  ")

        print(Fore.LIGHTWHITE_EX + "*" * one_side + Fore.RESET + Fore.LIGHTCYAN_EX + "  STATICS  " + Fore.RESET + Fore.LIGHTWHITE_EX + "*" * (space - 11 - one_side) + Fore.RESET)

        one_side = Menu.fitting(space, "  General Score Graph(1)  ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + ">" + Fore.RESET + Fore.LIGHTWHITE_EX  + "  General Score Graph(1)  " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * int((space - 27 - one_side)) + Fore.RESET)

        one_side = Menu.fitting(space, "  Score Graph For Each Quiz(2)  ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + ">" + Fore.RESET + Fore.LIGHTWHITE_EX + "  Score Graph For Each Quiz(2)  " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * int(
            (space - 33 - one_side)) + Fore.RESET)

        one_side = Menu.fitting(space, "  General Analyzes(3)  ")

        print(Fore.LIGHTCYAN_EX + "-" * int(one_side - 1) + Fore.RESET + Fore.LIGHTWHITE_EX + ">" + "  General Analyzes(3)  " + Fore.RESET + Fore.LIGHTCYAN_EX + "<" + "-" * int((space - 23 - one_side)) + Fore.RESET)

        statics_option = input("Please select one (1/2/3): ")

        # controls if user want back to menu
        if statics_option.lower() == "menu":
            return "m"

        # gather all data about information on quizzes solved by the user into data
        data = user.get_user_findata()
        # for first of statics
        if statics_option.upper() == "1":
            print()
            average_for_com = 0
            average_for_num = 0
            average_for_soft = 0
            # to count how times user play the quiz for each category
            count_com = 0
            count_num = 0
            count_soft = 0

            # information on quizzes solved by the user is specified by categories
            for line in data:
                if "components" == line[0].lower():
                    count_com += 1
                    # scores is collected
                    average_for_com += float(line[3])
                elif "number_systems" == line[0].lower():
                    count_num += 1
                    average_for_num += float(line[3])
                elif "software" == line[0].lower():
                    count_soft += 1
                    average_for_soft += float(line[3])

            # if the user has never played the quiz of category, the operation is not runned
            if count_num != 0:
                average_for_num /= count_num

            if count_soft != 0:
                average_for_soft /= count_soft

            if count_com != 0:
                average_for_com /= count_com

            # to show graphic, data is determined
            categories = ["Components", "Number_Systems", "Software"]
            percentages = [average_for_com, average_for_num, average_for_soft]

            # if the user has never played, the graph is not showed. But if the user played, the graph is showed
            if percentages != [0, 0, 0]:
                print("           **This chart shows the average of your scores in each category**")
                print()
                Menu.graph_plot(categories, percentages)
                print()

            else:
                print("COME HERE AFTER PLAY GAME")

            input("Please, enter to back menu")
            print()
            return "m"

        # for first of statics
        # shows the last three score and highest score of the user with graph for each category
        elif statics_option.upper() == "2":
            print()
            print("* Components(1)")
            print("* Number_Systems(2)")
            print("* Software(3)")

            quiz_name = input("Which Quiz? (1/2/3) ")

            components_lst = []
            number_systems_lst = []
            software_lst = []

            for line in data:
                if "components" == line[0].lower():
                    components_lst.append(line[3])
                elif "number_systems" == line[0].lower():
                    number_systems_lst.append(line[3])
                elif "software" == line[0].lower():
                    software_lst.append(line[3])

            # the last three score of quizzes of categories is gathered into these list.
            components_for_show = components_lst[-3:]
            number_systems_for_show = number_systems_lst[-3:]
            software_for_show = software_lst[-3:]

            data = user.get_user_findata()
            type_lst = []

            a = ""
            if quiz_name.upper() == "1":
                for line in data:
                    if "COMPONENTS" == line[0]:
                        type_lst.append(line)

                a = Menu.statics_2(type_lst, components_for_show)

            elif quiz_name.upper() == "2":
                for line in data:
                    if "NUMBER_SYSTEMS" == line[0]:
                        type_lst.append(line)

                a = Menu.statics_2(type_lst, number_systems_for_show)

            elif quiz_name.upper() == "3":
                for line in data:
                    if "SOFTWARE" == line[0]:
                        type_lst.append(line)

                a = Menu.statics_2(type_lst, software_for_show)

            if a == "m":
                return "m"

        # for third of statics
        # finds highest score, highest number of true and the shortest timing
        elif statics_option.upper() == "3":
            print()
            print("* Components (1)")
            print("* Number_Systems (2)")
            print("* Software (3)")

            quiz_name = input("Which Quiz (1/2/3) ?")

            if quiz_name.upper() == "1":
                Menu.found_general_analyzes("COMPONENTS", user)

            elif quiz_name.upper() == "2":
                Menu.found_general_analyzes("NUMBER_SYSTEMS", user)

            elif quiz_name.upper() == "3":
                Menu.found_general_analyzes("SOFTWARE", user)

            a = input("Please, enter to back menu")
            time.sleep(1)
            print()
            return "m"

    @staticmethod
    def found_general_analyzes(type, user):
        type_lst = []
        data = user.get_user_findata()
        for line in data:
            if type == line[0]:
                type_lst.append(line)

        # controls the user has ever played quiz of the type
        # firstly, assigns the first data to all variables
        # and assigns all data about the issue to these listes
        if type_lst:
            lst_for_score = type_lst[0]
            high_score = float(type_lst[0][3])
            lst_for_true = type_lst[0]
            high_true = int(type_lst[0][1])
            lst_for_timing = type_lst[0]
            best_timing = float(type_lst[0][4])

            # to find the hishest score
            for lst in type_lst:
                if float(lst[3]) >= high_score:
                    high_score = float(lst[3])
                    lst_for_score[0], lst_for_score[1], lst_for_score[2], lst_for_score[3], lst_for_score[4] = lst[
                                                                                                                   0], int(
                        lst[1]), int(lst[2]), float(lst[3]), float(lst[4])

            print(
                f"Your highest score: {high_score:15.2f}\t\t//\t\tT: {lst_for_score[1]}\tF: {lst_for_score[2]:10}\tTime: {lst_for_score[4]:7.2f}")

            # to find the highest number of true
            for lst in type_lst:
                if int(lst[1]) >= high_true:
                    high_true = int(lst[1])
                    lst_for_true[0], lst_for_true[1], lst_for_true[2], lst_for_true[3], lst_for_true[4] = lst[0], int(
                        lst[1]), int(lst[2]), float(lst[3]), float(lst[4])
            print(
                f"Your highest number of true: {high_true:6}\t\t//\t\tF: {lst_for_true[2]}\tScore: {lst_for_true[3]:.2f}\tTime: {lst_for_true[4]:7.2f}")

            # to find the shortest timing
            for lst in type_lst:
                if float(lst[4]) <= best_timing:
                    best_timing = float(lst[4])
                    lst_for_timing[0], lst_for_timing[1], lst_for_timing[2], lst_for_timing[3], lst_for_timing[4] = lst[
                                                                                                                        0], int(
                        lst[1]), int(lst[2]), float(lst[3]), float(lst[4])

            print(
                f"Your best time: {best_timing:19.2f}\t\t//\t\tT: {lst_for_timing[1]}\tF: {lst_for_timing[2]:10}\tScore: {lst_for_timing[3]:.2f}")

        else:
            print("COME HERE AFTER PLAY GAME")

    @staticmethod
    def show_rules(user):
        print()
        name = user.name
        space = 40 + len(user.name)

        one_side = int(Menu.fitting(space, "  RULES  "))
        print(Fore.LIGHTWHITE_EX + "*" * one_side + Fore.RESET + Fore.LIGHTCYAN_EX + "  RULES  " + Fore.RESET + Fore.LIGHTWHITE_EX + "*" * (space - 11 - one_side) + Fore.RESET)
        print()
        print("You can learn and enjoy with these quizes!!!", end="\n\n")

        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} There will be 12 question, and there will be 4 option for each question", end="\n\n")
        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} At the beginning, you have two joker. If you know first three question, you have one more joker!!!",
              end="\n\n")
        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} You can only use each joker one time", end="\n\n")
        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} {Fore.LIGHTWHITE_EX}Jokers:{Fore.RESET}")
        print("    Half-and-half : System eliminate two option that are wrong")
        print("    Answer twice: You have two right to find true answer")
        print(
            "    Change question: You can change the question with extra one, but you can not know whether the question is easier or not",
            end="\n\n")
        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} If you want use joker, you should write 'joker' to answer space", end="\n\n")
        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} If you want back to menu, write 'menu' or if you want quit, write 'quit'", end="\n\n")
        print(
            f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} Finally, you will have score which be calculated with your number of corrects and mistakes and timing",
            end="\n\n")
        print(f"{Fore.LIGHTCYAN_EX}***{Fore.RESET} If you want to see graphics about your results, you can look at the statics part")

        print()
        input("Please, enter to back menu")
        print()
        return "m"