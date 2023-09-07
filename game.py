from question import Question
import time
import sys
import random
from colorama import Fore


class Game:

    @staticmethod
    def play_quiz_it(user):
        # questions which about each category is taken thank to method get data in Class Question
        components_questions, number_systems_questions, software_questions = Question.get_data()
        # ctg is a variable which keep category the user prefer
        ctg = Game.show_n_pick_categories()
        # controls if user want to quit or back to menu
        check, a = Game.check_input(ctg)
        if a == "m":
            return "m"
        true_c = 0
        wrong_c = 0
        timing = 0.0
        score = 0.0
        # information that users give correct or wrong answers to each question will be collected.
        answer_lst = []
        lst_joker = ["half-and-half (hh)", "answer twice (tw)"]
        # for the component category
        if ctg.upper() == "1":
            for index, question in enumerate(components_questions):
                # there is 13 question in data, but 12 question is showed. The last question is for joker.
                # Therefore, the for loop stops after 12 question is showed
                if index == 12:
                    break
                # the method named Game.for_each_question is used for each question
                true_c, wrong_c, timing = Game.for_each_question(question, lst_joker, answer_lst, components_questions,
                                                                 timing, true_c, wrong_c, user)
                # controls if user want to quit or back to menu
                if true_c == "m":
                    return "m"
            # the method named Game.calculate_score is used to calculate score of quiz
            score = Game.calculate_score(true_c, wrong_c, timing)
            # the method named user.write_user_finish is used to write information about quiz to file
            user.write_user_finish(["COMPONENTS", true_c, wrong_c, score, timing])

        # for the number_systems category
        elif ctg.upper() == "2":
            for index, question in enumerate(number_systems_questions):
                # there is 13 question in data, but 12 question is showed. The last question is for joker.
                # Therefore, the for loop stops after 12 question is showed
                if index == 12:
                    break
                # the method named Game.for_each_question is used for each question
                true_c, wrong_c, timing = Game.for_each_question(question, lst_joker, answer_lst,
                                                                 number_systems_questions,
                                                                 timing, true_c, wrong_c, user)
                # controls if user want to quit or back to menu
                if true_c == "m":
                    return "m"
            # the method named Game.calculate_score is used to calculate score of quiz
            score = Game.calculate_score(true_c, wrong_c, timing)
            # the method named user.write_user_finish is used to write information about quiz to file
            user.write_user_finish(["NUMBER_SYSTEMS", true_c, wrong_c, score, timing])

        # for the software category
        elif ctg.upper() == "3":
            for index, question in enumerate(software_questions):
                # there is 13 question in data, but 12 question is showed. The last question is for joker.
                # Therefore, the for loop stops after 12 question is showed
                if index == 12:
                    break
                # the method named Game.for_each_question is used for each question
                true_c, wrong_c, timing = Game.for_each_question(question, lst_joker, answer_lst, software_questions,
                                                                 timing, true_c, wrong_c, user)
                # controls if user want to quit or back to menu
                if true_c == "m":
                    return "m"
            # the method named Game.calculate_score is used to calculate score of quiz
            score = Game.calculate_score(true_c, wrong_c, timing)
            # the method named user.write_user_finish is used to write information about quiz to file
            user.write_user_finish(["SOFTWARE", true_c, wrong_c, score, timing])

        print()
        print(f"{Fore.LIGHTCYAN_EX}Your score : {score}")
        print(f"T: {true_c}")
        print(f"F: {wrong_c}{Fore.RESET}")
        print()
        input("Please, enter to back menu")
        print()
        return "m"

    @staticmethod
    def for_each_question(question, lst_joker, answer_lst, type_questions, timing, true_c, wrong_c, user):
        print()
        # the time is taken when the question is displayed
        start = time.time()
        question.display_question()
        # user' answer is considered in the method named Game.using_joker
        end, is_true = Game.using_joker(lst_joker, answer_lst, question, type_questions, start, user)
        # controls if user want to quit or back to menu
        if end == "m":
            return "m", "m", "m"
        # the time is calculated when the user answer the question
        timing += end - start
        print(f"{Fore.LIGHTWHITE_EX}{timing}{Fore.RESET}")
        # if the user know first three question, the user gain one more joker right
        if answer_lst == ["T", "T", "T"]:
            print()
            print(f"{Fore.LIGHTWHITE_EX}CONGRATS!! YOU MADE A COMBO!! YOU HAVE ONE MORE JOKER!!{Fore.RESET}")
            print(f"{Fore.LIGHTCYAN_EX}-->{Fore.RESET} {Fore.LIGHTWHITE_EX}CHANGE QUESTION : You can change "
                  "the question with extra one, but you can not know whether the question is easier or not. Good "
                  f"Luck!! {Fore.RESET}")
            # the joker is added to joker list
            lst_joker.append("change question (cq)")
            time.sleep(1)
        # number of true is increase by 1 if answer of user is true
        true_c += 1 if is_true else 0
        # number of wrong is increase by 1 if answer of user is wrong
        wrong_c += 1 if not is_true else 0
        time.sleep(1)
        return true_c, wrong_c, timing

    @staticmethod
    def using_joker(lst_joker, answer_lst, question, question_lst, start, user):
        # controls what is the answer
        is_true, ans_q = question.answer_q(input(f"{Fore.LIGHTCYAN_EX}-->:{Fore.RESET}"))
        # controls if user want to quit or back to menu
        check, a = Game.check_input(ans_q)
        if a == "m":
            return "m", False
        end = 0.0
        # controls if user want to use joker
        if ans_q.upper() == "JOKER":
            print("JOKERS :", end=" ")
            # to show jokers that user can use
            if lst_joker:
                for joker in lst_joker:
                    print("*" + joker, end=" ")

                # system eliminate two option that are wrong with this joker
                cho_jok = input("WHICH ONE?" if len(lst_joker) >= 2 else "")
                if cho_jok.lower() == "hh":
                    # the method is used to print just true option and the other option which is picked randomly with
                    # question
                    question.display_half()
                    # user can not use same joker again
                    lst_joker.remove("half-and-half (hh)")
                    # controls what is the answer
                    is_true, answer = question.answer_q(input("--> "))
                    # the time is taken when the user answer the question
                    end = time.time()
                    # reaction is given depend on answer
                    Game.check_answer(is_true, answer_lst)
                    user.write_user_data([question.type, question.question, question.true_answer, answer, end - start])

                # user have two right to find true answer thanks to this
                elif cho_jok.lower() == "tw":
                    # user can not use same joker again
                    lst_joker.remove("answer twice (tw)")
                    is_true, answer = question.answer_q(input("Please enter your first answer --> "))
                    # controls what is the answer
                    if is_true:
                        print("Well done, true answer!!")
                        answer_lst.append("T")
                    # if the first answer is wrong, system ask again
                    else:
                        print("That's not true. Let's try again.")
                        # controls what is the answer
                        is_true, answer = question.answer_q(input("Please enter your second answer --> "))
                        if is_true:
                            print("Super.")
                            answer_lst.append("T")
                        else:
                            print("Ups! Wrong")
                            answer_lst.append("F")
                    # the time is taken when the user answer the question
                    end = time.time()
                    user.write_user_data([question.type, question.question, question.true_answer, answer, end - start])

                # user can change the question with extra one thanks to this joker
                elif cho_jok.lower() == "cq":
                    # user can not use same joker again
                    lst_joker.remove("change question (cq)")
                    # the question which last question in the list of type of quiz
                    question = question_lst[-1]
                    question.display_question()
                    # controls what is the answer
                    is_true, answer = question.answer_q(input("--> "))
                    # the time is taken when the user answer the question
                    end = time.time()
                    # reaction is given depend on answer
                    Game.check_answer(is_true, answer_lst)
                    user.write_user_data([question.type, question.question, question.true_answer, answer, end - start])

            else:
                is_true, ans_q = question.answer_q(input(f"{Fore.LIGHTCYAN_EX}You have not any joker anymore. Please write answer.:{Fore.RESET}"))
                check, a = Game.check_input(ans_q)
                if a == "m":
                    return "m", False
                end = 0.0
                # the time is taken when the user answer the question
                end = time.time()
                # reaction is given depend on answer
                Game.check_answer(is_true, answer_lst)
                user.write_user_data([question.type, question.question, question.true_answer, ans_q, end - start])

        else:
            # the time is taken when the user answer the question
            end = time.time()
            # reaction is given depend on answer
            Game.check_answer(is_true, answer_lst)
            user.write_user_data([question.type, question.question, question.true_answer, ans_q, end - start])

        return end, is_true

    @staticmethod
    def calculate_score(n_true, n_false, timing):
        score = (n_true * 10 - n_false * 3 - (timing / 10))
        return score

    # if user want back to menu or want to quit from the game in somewhere in the game, user can thanks to this method
    @staticmethod
    def check_input(input):
        if input.lower() == "menu":
            return True, "m"
        elif input.lower() == "quit":
            sys.exit("See you later!!!")
        else:
            return False, input

    @staticmethod
    def check_answer(is_true, answer_lst):
        if is_true:
            answer_lst.append("T")
            # if user know the last three questions, the reaction is given randomly from the list.
            if answer_lst[-3:] == ["T", "T", "T"]:
                congrats = ["Fantastic.", "Hats off!", "Good job!", "You rock!", "Sensational.", "Nice going."]
                sentence = random.choice(congrats)
                print(Fore.LIGHTWHITE_EX + sentence, "True answer." + Fore.RESET)
            else:
                print(Fore.LIGHTWHITE_EX + "Well done, true answer!!" + Fore.RESET)

        else:
            print(Fore.LIGHTWHITE_EX + "Unfortunately, wrong answer..." + Fore.RESET)
            answer_lst.append("F")
        return answer_lst

    # when play option is chosen from menu, to show categories to user
    @staticmethod
    def show_n_pick_categories():
        print("*Components(1)")
        print("*Number_Systems(2)")
        print("*Software(3)")

        return input("Please select one (1/2/3) --> ").upper()