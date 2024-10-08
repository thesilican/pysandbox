# pysandbox

A python REPL but with an entire file. Type python expressions and evaluate them
in real time.

![Video demo of pysandbox](./docs/demo.mov)

I personally use it for symbolic algebra using sympy.

## Getting Started

Firstly you'll need to have installed python (obviously), vim, and tmux.

You'll also need to have any dependencies in `pysandbox.py` installed, by
default they are numpy and sympy.

Then type `./pysandbox` to start a pysandbox tmux session. You can now
edit `main.py` in the left pane, in the right pane all variables and expressions
will be live updated whenever you save the file.

Feel free to modify `pysandbox.py` with whatever imports or functions you find
useful.

## How it works

The idea is to have a python script (`watch.py`) that constantly watches
the `main.py` file for updates.
When the file is updated, we transform the file by adding `pysandbox_out` calls
after each expression and assignment AST node which will print out the value
in a pretty format.

[sympy]: https://www.sympy.org/en/index.html
