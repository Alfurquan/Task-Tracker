from dataclasses import dataclass, field, asdict
from enum import Enum

class TaskState(Enum):
    TODO = 'Todo'
    INPROGRESS = 'Inprogress'
    DONE = 'Done'

@dataclass
class Task:
    id : int = field(default=None, compare=False)
    summary: str = None
    owner: str = None
    state: TaskState = TaskState.TODO.value
    
    @classmethod
    def from_dict(cls, dict):
        return Task(**dict)
    
    def to_dict(self):
        return asdict(self)
