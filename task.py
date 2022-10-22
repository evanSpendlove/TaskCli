class Task:
    def __init__(self, status, priority, name, project, time_to_complete, energy_level, tags):
        self.status = status
        self.priority = priority
        self.name = name.strip()
        self.project = project.strip()
        self.time_to_complete = time_to_complete
        self.energy_level = energy_level
        self.tags = tags.strip().split(',')

    def priority_number(self):
        priorities = {'NOW': 9, '!!!': 3, '!!': 2, '!': 1}
        return priorities[self.priority]

    def __str__(self):
        return f"[{self.status}][{self.priority}] {self.name} | {self.project} | {self.time_to_complete}m | {self.energy_level} | {', '.join(self.tags)}"

    def __repr__(self):
        return self.__str__()
