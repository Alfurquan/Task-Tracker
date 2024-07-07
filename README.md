tasks 
=====

Project task tracking CLI application

Usage 
-----

Here's how it works

    $ task add Shopping --owner Mark
    $ task add Read a book --owner John
    $ task list
    $ ID   state   owner   summary      
      ────────────────────────────────── 
       1    Todo    Mark    Shopping     
       2    Todo    John    Read a book  

    $ task update --id 1 --owner Jim
    $ task list
    $ ID   state   owner   summary      
      ────────────────────────────────── 
       1    Todo    Jim    Shopping     
       2    Todo    John    Read a book
    
    $ task --help
    $ task --help

    Usage: task [OPTIONS] COMMAND [ARGS]...

    Task is a small command line task tracking application.

    ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ --version             -v        Retrieves version of the app                                                                 │
    │ --install-completion            Install completion for the current shell.                                                    │
    │ --show-completion               Show completion for the current shell, to copy it or customize the installation.             │
    │ --help                          Show this message and exit.                                                                  │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │ add      Adds a task to the task board                                                                                       │
    │ clear    Delete off all tasks                                                                                                │
    │ delete   Delete a task with given id.                                                                                        │
    │ finish   Finish a task with given id.                                                                                        │
    │ list     Gets a list of tasks, filtering by owner or state if provided.                                                      │
    │ start    Starts a task with given id.                                                                                        │
    │ update   Updates a task with given id. 