class Reader:
    def read_tasks(self, path: str):
        with open(path, 'r') as f:
            return f.read().strip().split('\n')
