# ToDo List Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
I want to be able to create myself tasks and save them to a list
I want to be able to get a list of all my complete or incomplete tasks
I also want to be able to mark all existing tasks as complete in bulk

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ ToDo List                  │
│ - todos                    │
│ - add(todo)                │
│ - incomplete               │
│   => [incomplete todos]    ┼
│ - complete                 │
│   => [complete todos]      │
│ - give_up                  │
└─────────────┬──────────────┘
              │owns a list of 
              │               
┌────────────────────────────┐
│ ToDo                       │
│ - mark_complete(todo)      │
│                            │
└────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
# File: lib/todo_list.py
class ToDoList:
    def __init__(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side-effects:
        #   Creates empty list all_todos = []
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class ToDo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a ToDo List and two ToDos
When we add those two todos
Those todos are reflected in the todo list
"""
mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
mylist.add(todo1)
mylist.add(todo2)
mylist.all_todos => ["Wash the dishes", "Mow the lawn"]

"""
Given a ToDo List and three added ToDos
When we mark two of those as complete and call complete()
Only completed todos are returned
"""
mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
todo3 = ToDo("Feed the cat")
mylist.add(todo1)
mylist.add(todo2)
mylist.add(todo3)
todo1.mark_complete()
todo3.mark_complete()
mylist.complete => ["Wash the dishes", "Feed the cat"]

"""
Given a ToDo List and three added ToDos
When we mark one of those as complete and call incomplete()
Only incomplete todos are returned
"""

mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
todo3 = ToDo("Feed the cat")
mylist.add(todo1)
mylist.add(todo2)
mylist.add(todo3)
todo1.mark_complete()
mylist.incomplete => ["Mow the lawn", "Feed the cat"]

"""
Given a ToDo List and two added ToDos
When we call giveup() all are marked as completed
"""
mylist = ToDoList()
todo1 = ToDo("Wash the dishes")
todo2 = ToDo("Mow the lawn")
mylist.add(todo1)
mylist.add(todo2)
mylist.give_up()
mylist.complete() => ["Wash the dishes", "Mow the lawn"]
todo1.complete == True
todo2.complete == True
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# class ToDo

"""
Given a todo with a task
The task is reflected in the task property
"""
todo1 = ToDo("Wash the dishes")
todo1.task => "Wash the dishes"

"""
Given a todo with a task
The complete property reflects the incomplete status
"""
todo1 = ToDo("Wash the dishes")
todo1.complete => False

"""
Given a todo with a task
Marking the task as complete updates the complete property
"""
todo1 = ToDo("Wash the dishes")
todo1.markcomplete()
todo1.complete => True

"""
Given a todo with an empty task
Raise an Exception error
"""
todo1 = ToDo("") => "Task must not be empty"

# class ToDo_List

"""
Given a todo list with no tasks
An empty list is created for all_todos
"""
mylist = ToDoList()
mylist.all_todos => []

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
