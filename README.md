# PyRiddle

## Introduction
Welcome to PyRiddle! This Python package offers a fun and interactive way to engage with riddles. Whether you're a teacher looking to spice up classroom activities, a developer building a puzzle game, or just someone who enjoys brain teasers, PyRiddle provides easy access to a variety of riddles.

## Features
- **Easy Access to Riddles**: Quickly retrieve riddles for use in games, educational content, or leisure.
- **Batch Riddle Retrieval**: Fetch multiple riddles at once, perfect for quizzes or riddle-based challenges.
- **No Repetition**: Enjoy a fresh experience each time until all riddles are exhausted.

## Installation
PyRiddle is simple to install via pip. Make sure you have Python installed, then run:
```bash
pip install pyriddle
```

## Quick Start

### Setup
#### CLI 
##### Single Riddle
- Commnad: pyriddle[returns a single riddle]
```bash
pyriddle
```
##### Multiple Riddle
- Command: pyriddle -c <count>
```bash
pyriddle -c $COUNT
```

#### Shell
```python
import pyriddle
print(pyriddle.get_riddle())
print(pyriddle.get_riddles(count=10))
```

### Play with your data by importing the riddle factory and initializing it:

```python
from pyriddle import riddle_factory

# Define a sample dictionary of riddles
data = {
    "What has keys but can't open locks?": ["Keyboard"],
    "What has words but never speaks?": ["Book"]
}

# Create riddle retrieval functions
get_riddle, get_riddles = riddle_factory(data)
```

## Retrieve a Riddle
Get a single riddle and display it:

```python
riddle = get_riddle()
print("Riddle: ", riddle['question'])
print("Answer: ", riddle['answer'])
```


This version aims to be user-friendly and informative, focusing on the practical uses of PyRiddle rather than the internal workings of the code.
