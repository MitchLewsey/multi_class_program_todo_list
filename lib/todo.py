class ToDo():
    def __init__(self, task):
        if task == "":
            raise Exception("Task must not be empty")
        self.task = task
        self.complete = False
        pass

    def mark_complete(self):
        self.complete = True