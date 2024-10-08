#!/usr/bin/env python
from argparse import ArgumentParser
import os
import ast
from time import sleep
from subprocess import run


def transform(source):
    """
    Transforms the input source code by adding pysandbox_out() calls after
    assignment statements and expressions, and pysandbox_print() at the end of
    the program.
    """

    def out_expr(id):
        return ast.Expr(
            value=ast.Call(
                func=ast.Name(id="pysandbox_out", ctx=ast.Load()),
                args=[ast.Name(id=id, ctx=ast.Load()), ast.Constant(value=id)],
                keywords=[],
            )
        )

    def print_expr():
        return ast.Expr(
            value=ast.Call(
                func=ast.Name(id="pysandbox_print", ctx=ast.Load()),
                args=[],
                keywords=[],
            )
        )

    # Parse AST
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        raise e

    # Apply node transformation
    nodes = []
    for node in tree.body:
        if isinstance(node, ast.Expr):
            nodes.append(out_expr(ast.unparse(node)))
        elif isinstance(node, ast.Assign):
            nodes.append(node)
            if isinstance(node.targets[0], ast.Name):
                nodes.append(out_expr(node.targets[0].id))
            elif isinstance(node.targets[0], ast.Tuple):
                for element in node.targets[0].dims:
                    if isinstance(element, ast.Name):
                        nodes.append(out_expr(element.id))
        else:
            nodes.append(node)

    # At the end of the program, add a pysandbox print call
    nodes.append(print_expr())

    # Return new source code
    new_tree = ast.Module(body=nodes, type_ignores=[])
    new_source = ast.unparse(new_tree)
    return new_source


def run_file(filepath):
    """Run the main.py file, first applying source code transformations"""
    os.system("clear")
    with open(filepath, "r") as f:
        raw_source = f.read()

    try:
        source = transform(raw_source)
    except Exception as e:
        print("Error parsing input:", e)
        return

    ret = run(["python", "-c", source])
    if ret.returncode != 0:
        print()
        for i, line in enumerate(source.splitlines()):
            print(f"{i + 1:>3} {line}")


def watch(filepath):
    """Watch the main python file for changes, if changed run the file"""
    try:
        last_time = None
        while True:
            try:
                curr_time = os.stat(filepath).st_mtime
            except FileNotFoundError:
                continue
            if last_time != curr_time:
                last_time = curr_time
                run_file(filepath)
            sleep(0.1)
    except KeyboardInterrupt:
        pass


def main():
    parser = ArgumentParser(prog="watch", description="Watch a CAS file")
    parser.add_argument(
        "filepath", help="The file to watch", nargs="?", default="main.py"
    )
    args = parser.parse_args()
    watch(args.filepath)


if __name__ == "__main__":
    main()
