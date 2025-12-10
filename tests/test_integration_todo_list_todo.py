from lib.todo_list import *
from lib.todo import *
import pytest

"""
Given a ToDo List and two ToDos
When we add those two todos
Those todos are reflected in the todo list
"""
def test_added_todos_are_added_to_list():
    mylist = ToDoList()
    todo1 = ToDo("Wash the dishes")
    todo2 = ToDo("Mow the lawn")
    mylist.add(todo1)
    mylist.add(todo2)
    actual = mylist.all_todos
    expected = ["Wash the dishes", "Mow the lawn"]
    assert actual == expected

"""
Given a ToDo List and three added ToDos
When we mark two of those as complete and call complete()
Only completed todos are returned
"""
def test_only_completed_tasks_returned_by_complete_list():
    mylist = ToDoList()
    todo1 = ToDo("Wash the dishes")
    todo2 = ToDo("Mow the lawn")
    todo3 = ToDo("Feed the cat")
    mylist.add(todo1)
    mylist.add(todo2)
    mylist.add(todo3)
    todo1.mark_complete()
    todo3.mark_complete()
    actual = mylist.complete
    expected = ["Wash the dishes", "Feed the cat"]
    assert actual == expected

"""
Given a ToDo List and three added ToDos
When we mark one of those as complete and call incomplete()
Only incomplete todos are returned
"""
def test_only_incomplete_tasks_returned_by_incomplete_list():
    mylist = ToDoList()
    todo1 = ToDo("Wash the dishes")
    todo2 = ToDo("Mow the lawn")
    todo3 = ToDo("Feed the cat")
    mylist.add(todo1)
    mylist.add(todo2)
    mylist.add(todo3)
    todo1.mark_complete()
    actual = mylist.complete
    expected = ["Mow the lawn", "Feed the cat"]
    assert actual == expected

"""
Given a ToDo List and two added ToDos
When we call giveup() all are marked as completed
"""
def test_give_up_marks_todos_completed():
    mylist = ToDoList()
    todo1 = ToDo("Wash the dishes")
    todo2 = ToDo("Mow the lawn")
    mylist.add(todo1)
    mylist.add(todo2)
    mylist.giveup()
    actual = mylist.complete()
    expected = ["Wash the dishes", "Mow the lawn"]
    assert actual == expected