"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id']) # Taskというnamedtuple, 属性名から要素にアクセス
Task.__new__.__defaults__ = (None, None, False, None) # __new__.__defaults__で未指定時のデフォルト値を予め指定できる

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access(): # Taskのメンバにインデックスでなく、名前でアクセス
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
