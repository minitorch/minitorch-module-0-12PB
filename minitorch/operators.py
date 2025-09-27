"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    "$f(x, y) = x * y$"
    return x * y


def id(x: float) -> float:
    "$f(x) = x$"
    return x


def add(x: float, y: float) -> float:
    "$f(x, y) = x + y$"
    return x + y


def neg(x: float) -> float:
    "$f(x) = -x$"
    return -x


def lt(x: float, y: float) -> float:
    "$f(x) =$ 1.0 if x is less than y else 0.0"
    return 1.0 if x < y else 0.0


def eq(x: float, y: float) -> float:
    "$f(x,y) =$ 1.0 if x is equal to y else 0.0"
    return 1.0 if x == y else 0.0


def max(x: float, y: float) -> float:
    "$f(x,y) =$ x if x is larger than y else y"
    return x if x > y else y


def is_close(x: float, y: float) -> float:
    "$f(x,y) =$ 1.0 if x and y are within 1.0 of each other, else 0.0 "
    diff = x - y
    return abs(diff) < 1


def sigmoid(x: float) -> float:
    "$f(x) = 1 / (1 + e^-x)$ "
    return 1 / (1 + math.e**(-x))


def relu(x: float) -> float:
    """
    $f(x) =$ x if x is greater than 0, else 0
    """
    return x if x > 0 else 0.0


def log(x: float) -> float:
    "$f(x) = log(x)$"
    return math.log(x)


def exp(x: float) -> float:
    "$f(x) = exp(x)$"
    return math.exp(x) 


def inv(x: float) -> float:
    "$f(x) = 1 / x$"
    return 1 / x


def log_back(x: float, y: float) -> float:
    "$f(x,y) = d/dx(log(x)) * y$"
    return x**(-1) * y


def inv_back(x: float, y: float) -> float:
    "$f(x,y) = d/dx * (1 / x) * y$"
    return x**(-2) * y


def relu_back(x: float, y: float) -> float:
    "$f(x,y) = d/dx(log(x)) * y$"
    return x * y if x > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(f: Callable, a: Iterable) -> list:
    """ Higher-order function that applies a given function
    to each element of an iterable 
    """
    result = []
    for element in a:
        result.append(f(a))
    return result


def zipWith(f: Callable, a: Iterable, b: Iterable) -> list:
    """
    Higher-order function that combines elements from two 
    iterables using a given function
    """
    return [f(element_a, element_b) for element_a, element_b in zip(a, b)]


def reduce(f: Callable, a: Iterable) -> float:
    """ Higher-order function that reduces an iterable to a single
    value using a given function
    """
    iterator = iter(a)
    result = next(iterator)
    for element in iterator:
        result = f(result, element)
    return result


def negList(a: Iterable) -> list:
    """ Negate all elements in a list using map
    """
    return map(neg, a)


def addList(a: Iterable, b: Iterable) -> list:
    """ Add corresponding elements from two lists using zipWith
    """
    return zipWith(add, a, b)


def sum(a: Iterable) -> float:
    """ Sum all elements in a list using reduce
    """
    return reduce(add, a)


def prod(a: Iterable) -> float:
    """ Calculate the product of all elements in a list using reduce
    """
    return reduce(mul, a)
