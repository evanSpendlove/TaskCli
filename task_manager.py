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
        print("1. Something important")
        print("2. Something easy")
        print("3. Something quick")
        print("4. Task Stats")
        print("")
        print("0. Exit")
        print("==========================")

    def choose_option(self):
        self.clear_screen()
        self.print_menu()
        handlers = [lambda : print("Invalid choice"), self.next_task, self.easy_task, self.quick_task, self.stats]
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

    def next_task(self):
        max_priority = max([t.priority_number() for t in self.tasks])
        for task in self.tasks:
            if task.priority_number() == max_priority:
                print(f"Your next task is: {task}")
                return

    def easy_task(self):
        for task in self.tasks:
            if task.energy_level == 'Low':
                print(f"Your easy task is: {task}")

    def quick_task(self):
        min_time = min([t.time_to_complete for t in self.tasks])
        for task in self.tasks:
            if task.time_to_complete == min_time:
                print(f"Your quick task is: {task}")

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

