# ds-algo-python-practice

## Table of Contents
- [Code](#code)
    - [Python virtual environment](#python-venv)

## Code

The code for this repository can be found in the directory: [src](src/).

The tests for the code for this repository can be found in the directory: [tests](tests/).

### Running tests

To run tests for the code, run the following command in the root directory of the repository:

```BASH
pytest tests/<test-file>.py
```

### Python virtual environment

Before using the code it is best to setup and start a Python virtual environment in order to avoid potential package clashes using the [requirements](requirements.txt) file:

```BASH
# Navigate into the project directory

# Create a virtual environment
python3 -m venv <venv>

# Activate virtual environment
source <venv>/bin/activate

# Install dependencies for code
pip3 install -r requirements.txt

# When finished with virtual environment
deactivate
```
