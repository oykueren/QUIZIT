import csv
import os


class User:

    def __init__(self, name):
        self.name = name
        self.data = []

    # gathers information on questions answered by each user into self.data from the file named user's name or
    # creates a file for this aim.
    def get_user_data(self):
        self.data = []
        # try open a file named user's nickname
        # If can not open, that means there is not the file. In that case, creates the file
        try:
            open(f"{self.name}.csv")
        except FileNotFoundError:
            open(f"{self.name}.csv", "x")

        os.chmod(f"{self.name}.csv", 0o777)

        # after opening the file, reads data in the file
        with open(f"{self.name}.csv") as f:
            user_reader = csv.reader(f)
            for index, line in enumerate(user_reader):
                if index % 2 == 0:  # uses this way because the information in the file is written with a blank line
                    # each item in lines is specified
                    type, question, answer, true_answer, time = line[0], line[1], line[2], line[3], line[4]
                    # information that is specified is assigned to self.data
                    self.data.append([type, question, answer, true_answer, time])

        return self.data

    # to write information on questions answered by the user to file named user's name or create a file for this aim
    def write_user_data(self, data_l):
        # try open a file named user's nickname
        # If can not open, that means there is not the file. In that case, creates the file to write
        try:
            open(f"{self.name}.csv", "r")
        except FileNotFoundError:
            open(f"{self.name}.csv", "w")

        os.chmod(f"{self.name}.csv", 0o777)

        with open(f"{self.name}.csv", "a") as f:
            user_writer = csv.writer(f)
            # each item on list data_l is specified
            type, question, answer, true_answer, time = data_l[0], data_l[1], data_l[2], data_l[3], data_l[4]
            # information that is specified is written to the file
            user_writer.writerow([type, question, answer, true_answer, time])

    # the method is created to gather all data about information on quizzes solved by the user into self.data
    # from the file named '(user's name)total' or creates a file for this aim.
    def get_user_findata(self):
        self.data = []
        # try open a file named (user's nickname).total
        # If can not open, that means there is not the file. In that case, creates the file
        try:
            open(f"{self.name}total.csv")
        except FileNotFoundError:
            open(f"{self.name}total.csv", "x")

        os.chmod(f"{self.name}total.csv", 0o777)

        # after opening the file, reads data in the file
        with open(f"{self.name}total.csv") as f:
            user_reader = csv.reader(f)
            for index, line in enumerate(user_reader):
                if index % 2 == 0:  # uses this way because the information in the file is written with a blank line
                    # each item in lines is specified
                    type, n_ture, n_false, score, timing = line[0], line[1], line[2], line[3], line[4]
                    # information that is specified is assigned to self.data
                    self.data.append([type, n_ture, n_false, score, timing])
        return self.data

    # to write information on quizzes solved by the user to file named (user's name)total or create a file for this aim
    def write_user_finish(self, fin_data):
        # try open a file named (user's name)total
        # If can not open, that means there is not the file. In that case, creates the file to write
        try:
            open(f"{self.name}total.csv", "r")
        except FileNotFoundError:
            open(f"{self.name}total.csv", "w")

        os.chmod(f"{self.name}total.csv", 0o777)

        with open(f"{self.name}total.csv", "a") as f:
            user_writer = csv.writer(f)
            # each item on list data_l is specified
            type, n_ture, n_false, score, timing = fin_data[0], fin_data[1], fin_data[2], fin_data[3], fin_data[4]
            # information that is specified is written to the file
            user_writer.writerow([type, n_ture, n_false, score, timing])
