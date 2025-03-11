# pysandbox

A python REPL but with an entire file. Type python expressions and evaluate them
in real time.

![Video demo of pysandbox](./docs/demo.mov)

I personally use it for symbolic algebra using sympy.

## Getting Started

### In the terminal
I use pysandbox primarily in the terminal using the `pysandbox` helper script.

You'll need the following installed:
- python (`python` needs to be in your path, if your distribution has `python3` in the path, edit it in `watch.py`)
- neovim (If you wish to use a different editor, change the editor variable in `pysandbox`)
- tmux
- Any python dependencies imported in `pysandbox.py`

Type `./pysandbox` to start a pysandbox tmux session. You can now
edit `main.py` in the left pane, in the right pane all variables and expressions
will be live updated whenever you save the file.

Feel free to modify `pysandbox.py` with whatever imports or functions you find useful.

### Any text editor

Create a filed named `main.py` in your editor that imports from `pysandbox.py`, for example:

```py
from pysandbox import *

# For demonstration purposes
x = 2
y = 3
x + y
```

Run `python watch.py` to see the output. All variables and expressions
will be live updated whenever you save the `main.py` file.

## How it works

The idea is to have a python script (`watch.py`) that constantly watches the `main.py` file for updates.
When the file is updated, we transform the file by adding `pysandbox_out` calls
after each expression and assignment AST node which will print out the value in a pretty format.
