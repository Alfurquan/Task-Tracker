class TasksException(Exception):
    pass


class MissingSummary(TasksException):
    pass

class MissingOwner(TasksException):
    pass

class InvalidTaskId(TasksException):
    pass