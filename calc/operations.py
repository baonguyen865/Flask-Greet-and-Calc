from flask import Flask, request

"""Basic math operations."""

def add(a, b):
    """Add a and b."""
    
    return a + b

def sub(a, b):
    """Substract b from a."""

    return a - b

def mult(a, b):
    """Multiply a and b."""

    return a * b

def div(a, b):
    """Divide a by b."""

    return a / b


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)