import re
from typing import List

from task import Task

TASK_REGEX = r"\[(TODO|DONE|WAITING)\]\[(NOW|!!!|!!|!|BACKLOG)\]\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([0-9]+)\s*\|\s*(High|Medium|Low)\s*\|\s+([a-zA-Z\s,]*)"

class Parser:
    def parse_task(self, task: str):
        matches = re.finditer(TASK_REGEX, task, re.MULTILINE)
        groups = []
        for match_num, task_match in enumerate(matches):
            if match_num > 0:
                raise Exception(f"Multiple matches found in task: {task}")
            groups = list(task_match.groups())
        return Task(*groups)

    def parse_tasks(self, tasks: List[str]):
        return list(map(self.parse_task, tasks))
