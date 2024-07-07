import typer
import importlib.metadata
import os
from io import StringIO
import rich
from typing import List
from pathlib import Path
from rich.table import Table
from .api import TaskAPI
from .task import Task


app = typer.Typer(no_args_is_help=True)

def version_callback(value: bool):
    """
    Retrieves version of the app.
    """
    if value:
        version = importlib.metadata.version('task-tracker')
        typer.echo(version)
        raise typer.Exit()
    
@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(
        None, "--version", "-v", callback=version_callback, help="Retrieves version of the app")
    ):
    """
    Task is a small command line task tracking application.
    """
    pass

@app.command()
def add(
    summary: List[str],
    owner: str = typer.Option(..., "--owner", "-o", help="Enter owner for task")
    ):
    """
    Adds a task to the task board
    """
    summary = " ".join(summary) if summary else None
    api = TaskAPI(get_path())
    api.add_task(Task(summary=summary, owner=owner))
    print("Task added !")

@app.command()
def list(
    owner: str = typer.Option(None, "--owner", "-o", help="Owner of the task"),
    state: str = typer.Option(None, "--state", "-s", help="State of task")
    ):
    """
    Gets a list of tasks, filtering by owner or state if provided.
    """
    api = TaskAPI(get_path())
    tasks = api.get_tasks(owner, state)
    table = Table(box=rich.box.SIMPLE)
    table.add_column("ID")
    table.add_column("state")
    table.add_column("owner")
    table.add_column("summary")
    for task in tasks:
        task = Task.from_dict(task)
        owner = "" if task.owner is None else task.owner
        table.add_row(str(task.id), task.state, owner, task.summary)
    out = StringIO()
    rich.print(table, file=out)
    print(out.getvalue())

@app.command()
def start(
    id : int = typer.Option(..., "--id", help="Id of the task to start")
    ):
    """
    Starts a task with given id.
    """
    api = TaskAPI(get_path())
    task = api.get_task(id)
    
    if task is None:
        print(f"Task with id {id} does not exists!")
        return
    
    api.start_task(task)
    print("Task started!")
    
@app.command()
def finish(
    id : int = typer.Option(..., "--id", help="Id of the task to finish")
    ):
    """
    Finish a task with given id.
    """
    api = TaskAPI(get_path())
    task = api.get_task(id)
    
    if task is None:
        print(f"Task with id {id} does not exists!")
        return
    
    api.end_task(task)
    print("Task finished!")

@app.command()
def update(
    id : int = typer.Option(..., "--id", help="Id of the task to update"),
    summary: List[str] = typer.Option(None, "-s", "--summary", help="Summary of task in quote string"),
    owner: str = typer.Option(None, "-o", "--owner", help="Owner of task")
    ):
    """
    Updates a task with given id.
    """
    api = TaskAPI(get_path())
    task = api.get_task(id)
    
    if task is None:
        print(f"Task with id {id} does not exists!")
        return
    
    task = Task.from_dict(task)
    summary = " ".join(summary) if summary else None
    
    task.summary = summary
    
    if owner is not None:
        task.owner = owner
    
    api.update_task(task)
    print("Task updated!")

@app.command()
def delete(
    id : int = typer.Option(..., "--id", help="Id of task to delete")
    ):
    """
    Delete a task with given id.
    """
    api = TaskAPI(get_path())
    task = api.get_task(id)
    
    if task is None:
        print(f"Task with id {id} does not exists!")
        return
    
    api.delete_task(Task.from_dict(task))
    print("Task deleted!")
 
@app.command()
def clear():
    """
    Delete off all tasks
    """
    api = TaskAPI(get_path())
    api.clear_tasks()
    print("All tasks cleared!")
    
def get_path():
    db_path_env = os.getenv("CARDS_DB_DIR", "")
    if db_path_env:
        db_path = Path(db_path_env)
    else:
        db_path = Path.home() / "task_db"
    return db_path