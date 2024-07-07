from .db import DB
from .exception import MissingSummary, MissingOwner, InvalidTaskId
from .task import Task, TaskState

class TaskAPI:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path=db_path, db_file_prefix='.task_db', table_name='task')
        
    def add_task(self, task: Task) -> int:
        if not task.summary:
            raise MissingSummary
        
        if not task.owner:
            raise MissingOwner
        
        id = self._db.create(task.to_dict())
        self._db.update(id, {"id": id})
        self._db.close()
        return id
    
    def get_tasks(self, owner: str, state: str):
        tasks = self._db.list()
        self._db.close()
        
        filtered_tasks = tasks
        if owner is not None:
            filtered_tasks = [task for task in tasks if task["owner"].lower() == owner.lower()]

        if state is not None:
            filtered_tasks = [task for task in tasks if task["state"].lower() == state.lower()]
        
        return filtered_tasks
    
    def get_task(self, id):
        return self._db.get(id)
    
    def start_task(self, task_to_start: dict):
        task = Task.from_dict(task_to_start)
        task.state = TaskState.INPROGRESS.value
        self._db.update(task.id, task.to_dict())
        
    def end_task(self, task_to_end: dict):
        task = Task.from_dict(task_to_end)
        task.state = TaskState.DONE.value
        self._db.update(task.id, task.to_dict())
    
    def update_task(self, task: Task):
        self._db.update(task.id, task.to_dict())
    
    def delete_task(self, task: Task):
        self._db.delete(task.id)
    
    def clear_tasks(self):
        self._db.clear()
    
    def close_connection(self):
        self._db.close()
    