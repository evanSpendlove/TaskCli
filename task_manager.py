from collections import Counter
from subprocess import call

from config import *
from reader import Reader
from parser import Parser
from task import Task

class TaskManager:
    def __init__(self, task_path: str):
        reader = Reader()
        parser = Parser()

        self.tasks = parser.parse_tasks(reader.read_tasks(task_path))
        self.valid_choices = [0, 1, 2, 3, 4]

    def clear_screen(self):
        _ = call('clear')

    def print_menu(self):
        print("==== TASK MANAGER MENU ====")
        print("1. Top N important")
        print("2. Top N easy")
        print("3. Top N quick")
        print("4. Task Stats")
        print("")
        print("0. Exit")
        print("==========================")

    def choose_option(self):
        self.clear_screen()
        self.print_menu()
        handlers = [lambda : print("Invalid choice"), lambda: self.top_n('priority'), lambda: self.top_n('energy'), lambda: self.top_n('time'), self.stats]
        option = int(input("\nChoose the next operation: "))
        print()
        if option not in self.valid_choices:
            print(f"Error: invalid choice, please select one of {self.valid_choices}")
            return -2
        elif option == 0:
            "Exiting..."
            return -1
        else:
            handlers[option]()
            return 0

    def ask_again(self):
        while True:
            again = input("Continue? (Y/N): ")
            if again not in ['Y', 'N']:
                print("Error, invalid choice, please choose one of [Y, N]")
            else:
                break
        return again == "Y"

    def run(self):
        again = True
        choice = -2
        while again:
            while choice == -2:
                choice = self.choose_option()

            if choice == -1:
                return
            again = self.ask_again()
            choice = -2

    def ask_for_n(self):
        n = 1
        while True:
            n = int(input("How many tasks? (up to 10): "))
            if n not in [1,2,3,4,5,6,7,8,9,10]:
                print("Error, invalid choice, please choose an integer between 1, 10 inclusive")
            else:
                break
        return n

    def top_n(self, attribute: str):
        keys = { 'priority': lambda task: task.priority_number(),
                'energy': lambda task: task.energy_level,
                'time': lambda task: task.time_to_complete }

        n = self.ask_for_n()
        tasks = self.sort_by(keys[attribute])[:n]
        tasks = '\n'.join([str(t) for t in tasks])

        if len(tasks) == 0:
            print(f"Your task is: {tasks[0]}")
        else:
            print(f"Your tasks are:\n{tasks}")

    def sort_by(self, key):
        return list(sorted(self.tasks, key=key))

    def stats(self):
        total_tasks = len(self.tasks)
        task_priorities = Counter([t.priority for t in self.tasks])

        print("\n--- Task Summary ---")
        print(f"Total tasks: {total_tasks}")
        print(f"Ultra High Priority tasks: {task_priorities['NOW']}")
        print(f"High Priority tasks: {task_priorities['!!!']}")
        print(f"Medium Priority tasks: {task_priorities['!!']}")
        print(f"Low Priority tasks: {task_priorities['!']}")
        print("---------------------")

