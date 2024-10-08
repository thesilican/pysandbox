import math
import re
import os
import collections
import random
import numpy as np
import itertools
import sympy as sym
import sympy.plotting
import sympy.abc
import sympy.stats


from collections import Counter
from collections.abc import Iterable
from random import randint
from itertools import combinations, permutations, product, combinations_with_replacement
from sympy.abc import *
from sympy import (
    # Basic
    S,
    Eq,
    Piecewise,
    Lambda,
    Sum,
    Function,
    # Functions
    sqrt,
    exp,
    log,
    # Trigonometry
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    pi,
    # Complex Numbers
    I,
    # Calculus
    limit,
    diff,
    idiff,
    integrate,
    Derivative,
    Integral,
    oo,
    E,
    # Linear Algebra
    Matrix,
    eye,
    # Differential Calculus
    Heaviside,
    # Statistics
    binomial,
    factorial,
    # Solve
    solve,
    dsolve,
    laplace_transform,
    apart,
)
from sympy.plotting import (
    plot,
    plot_implicit,
    plot_parametric,
    plot3d,
    plot3d_parametric_line,
    plot3d_parametric_surface,
    textplot,
)
from sympy.printing import print_latex, pretty
from sympy.logic.boolalg import (
    Not,
    And,
    Or,
    Nand,
    Nor,
    Xor,
    Xnor,
    Implies,
    Equivalent,
    true,
    false,
    truth_table,
    to_cnf,
)

sym.init_printing()


def frac(x, y):
    """
    Creates the fraction x / y. If both x and y are python primitives, we return
    a sympy fraction object instead to preserve precision.
    """
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return sym.Rational(x, y)
    else:
        return x / y


_out_values = []


def pysandbox_out(value, label):
    """
    Adds a value to the list of things printed by pysandbox
    """
    MAX_LABEL_LEN = 25
    label = str(label).strip()
    if len(label) > MAX_LABEL_LEN:
        label = label[: MAX_LABEL_LEN - 1] + "…"

    lines = pretty(value).splitlines()
    _out_values.append((label, lines))


def pysandbox_print():
    """
    Called at the end of the program to print all values added to the out list
    """
    if len(_out_values) == 0:
        print(" Welcome to PySandbox!\n\n Type some code in main.py to get started.")
        return
    label_len = max(len(label) for label, _ in _out_values)
    output_lines = []
    for label, lines in _out_values:
        center = len(lines) // 2
        for i, line in enumerate(lines):
            if i == center:
                output_lines.append(" " + label.rjust(label_len) + " = " + line)
            else:
                output_lines.append(" " * (label_len + 4) + line)
        output_lines.append("")
    print("\n".join(output_lines))
