# What is it?

A basic python / pytest project, all set-up and ready to go for you <3.


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
