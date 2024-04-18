# src/pyriddle/__init__.py
from .pyriddle import riddle_factory
from .data import data

get_riddle, get_riddles = riddle_factory(data)
