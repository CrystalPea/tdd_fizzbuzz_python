# What is it?

A basic python / pytest project, all set-up and ready to go for you <3.

# Instructions

Write a programme that simulates ‘rock paper scissors’

## Rules:
Each player chooses a move: either Rock, Paper, or Scissors. When both have selected the following rules are applied to determine the winner:

* Rock beats Scissors (it crushes them :d)
* Scissors beat Paper (they cut it!)
* Paper beats Rock (it covers it :))
* Both players choosing the same move results in a draw

Start by implementing the logic. If you get chance you can extend the programme by making it interactive and adding a UI


# Use it

Clone the repository.

Install, create, and activate your virtual environment:
```
sudo easy_install virtualenv
virtualenv venv
source ./venv/bin/activate
```

Install the dependencies:
```
pip install -r requirements.txt
```


Run `pytest -v` - you should get:

```
tests/test_blimey.py::test_two_times_two_equals_four PASSED
tests/test_blimey.py::TestBlimey::test_blimey_increases_by_9000 PASSED
```

Dispose of example code and start writing your code.

### Attention:
Whenever you add / delete a file / class, remember to update your `__init__.py` file accordingly.
