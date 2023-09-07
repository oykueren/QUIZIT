import csv
import random
from colorama import Fore


class Question:

    def __init__(self, type, question, answers, true_answer):
        self.type = type
        self.question = question
        self.answers = list(answers)
        self.true_answer = true_answer.upper()

    # to detect user's answer
    def answer_q(self, answer_u):
        if answer_u == "joker":
            return False, "JOKER"
        if answer_u.upper() == self.true_answer:
            return True, answer_u
        return False, answer_u

    # to create oprion for questions
    @staticmethod
    def option_creator(index):
        option_list = ["a", "b", "c", "d"]

        return option_list[index].upper()


    def display_question(self):
        print(f"{Fore.LIGHTCYAN_EX}--*{Fore.RESET} {self.question}")

        # to show options of questions with their indicator in order
        for index, answer in enumerate(self.answers):
            print(f"{Question.option_creator(index)}) {answer}")

    # for half-and-half joker
    def display_half(self):
        options = ["A", "B", "C", "D"]
        # there is if-elif conditionals for probability of each option being correct
        if options[0] == self.true_answer:
            # to pick an option without true answer
            other = random.choice(["B", "C", "D"])
            other_answer = None

            # to assign information of options
            if other == "B":
                other_answer = self.answers[1]
            elif other == "C":
                other_answer = self.answers[2]
            elif other == "D":
                other_answer = self.answers[3]
            print(self.question)
            # to print just true option and the other option which is picked above
            for answer in options:
                if answer != self.true_answer and answer != other:
                    print()
                if answer == other:
                    print(f"{other}) {other_answer}")
                if answer == self.true_answer:
                    print(f"A) {self.answers[0]}")

        elif options[1] == self.true_answer:
            # to pick an option without true answer
            other = random.choice(["A", "C", "D"])
            other_answer = None

            # to assign information of options
            if other == "A":
                other_answer = self.answers[0]
            elif other == "C":
                other_answer = self.answers[2]
            elif other == "D":
                other_answer = self.answers[3]
            print(self.question)

            # to print just true option and the other option which is picked above
            for answer in options:
                if answer != self.true_answer and answer != other:
                    print()
                if answer == other:
                    print(f"{other}) {other_answer}")
                if answer == self.true_answer:
                    print(f"B) {self.answers[1]}")

        elif options[2] == self.true_answer:
            # to pick an option without true answer
            other = random.choice(["A", "B", "D"])
            other_answer = None

            # to assign information of options
            if other == "A":
                other_answer = self.answers[0]
            elif other == "B":
                other_answer = self.answers[1]
            elif other == "D":
                other_answer = self.answers[3]
            print(self.question)

            # to print just true option and the other option which is picked above
            for answer in options:
                if answer != self.true_answer and answer != other:
                    print()
                if answer == other:
                    print(f"{other}) {other_answer}")
                if answer == self.true_answer:
                    print(f"C) {self.answers[2]}")

        elif options[3] == self.true_answer:
            # to pick an option without true answer
            other = random.choice(["A", "B", "C"])
            other_answer = None

            # to assign information of options
            # to assign information of options
            if other == "A":
                other_answer = self.answers[0]
            elif other == "C":
                other_answer = self.answers[2]
            elif other == "B":
                other_answer = self.answers[1]
            print(self.question)

            # to print just true option and the other option which is picked above
            for answer in options:
                if answer != self.true_answer and answer != other:
                    print()
                if answer == other:
                    print(f"{other}) {other_answer}")
                if answer == self.true_answer:
                    print(f"D) {self.answers[3]}")

    # to take information of questions from file named data
    @staticmethod
    def get_data():
        # empty lists is created to assign information about every one question to the list in its category.
        components_questions = []
        number_systems_questions = []
        software_questions = []

        # assigns all the data to reader variable by opening file
        with open("../data.csv") as file:
            reader = csv.reader(file)
            for index, line in enumerate(reader):
                if not line:
                    break
                if index == 0:
                    continue
                # determines which item in reader is which information of the question
                type = line[0]
                question = line[1]
                a = line[2]
                b = line[3]
                c = line[4]
                d = line[5]
                answer = line[-1]

                # all information about each question is sent to Clas Question to use
                # all options for one question is gathered into a list
                question = Question(type, question, [a, b, c, d], answer)

                # to assign information about every one question to the list in its category
                if "components" in type:
                    components_questions.append(question)
                elif "number_systems" in type:
                    number_systems_questions.append(question)
                elif "software" in type:
                    software_questions.append(question)

        return components_questions, number_systems_questions, software_questions
