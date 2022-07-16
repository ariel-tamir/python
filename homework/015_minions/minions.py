from minion import Minion


class Minions:
    def __init__(self):
        self.minions_list = []

    def add_from_file(self):
        file_name = input("Enter file name:")
        with open(file_name, "r") as user_file:
            for line in user_file:
                minion = Minion(line)
                self.minions_list.append(minion)

    def save_minions_to_file(self):

    def list_minions(self):

    def assign_job(self):

    def report_job_complete(self):

