# r_like.py
import math
from fractions import Fraction
import matplotlib.pyplot as plt


def choose(n, k, formatted=False):
    """
    Calculate the number of combinations (n choose k).

    Args:
        n (int): Total number of items.
        k (int): Number of items to choose.
        formatted (bool): If True, returns the result as a formatted string with commas.

    Returns:
        int or str: Number of combinations, formatted as a string if formatted is True.
    """
    result = math.comb(n, k)
    if formatted:
        return f"{result:,}"
    return result

def seq(start, stop, step=1):
    """
    Generate a sequence of numbers.

    Args:
        start (int): Starting number of the sequence.
        stop (int): Ending number of the sequence.
        step (int): Step size between numbers in the sequence.

    Returns:
        list: A list of numbers in the sequence.
    """
    return list(range(start, stop + 1, step))

def mean(values):
    """
    Calculate the mean of a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        float: The mean of the list of numbers.
    """
    return sum(values) / len(values)

def median(values):
    """
    Calculate the median of a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        float: The median of the list of numbers.
    """
    sorted_values = sorted(values)
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]

def sd(values):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        float: The standard deviation of the list of numbers.
    """
    mean_val = mean(values)
    return math.sqrt(sum((x - mean_val) ** 2 for x in values) / (len(values) - 1))

def var(values):
    """
    Calculate the variance of a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        float: The variance of the list of numbers.
    """
    mean_val = mean(values)
    return sum((x - mean_val) ** 2 for x in values) / (len(values) - 1)

def sum_values(values):
    """
    Calculate the sum of a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        float: The sum of the list of numbers.
    """
    return sum(values)

def prod(values):
    """
    Calculate the product of a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        float: The product of the list of numbers.
    """
    result = 1
    for value in values:
        result *= value
    return result

def summary(values):
    """
    Provide summary statistics for a list of numbers.

    Args:
        values (list): List of numbers.

    Returns:
        dict: Summary statistics including min, max, mean, median, sd, var, sum, and count.
    """
    return {
        'min': min(values),
        'max': max(values),
        'mean': mean(values),
        'median': median(values),
        'sd': sd(values),
        'var': var(values),
        'sum': sum_values(values),
        'prod': prod(values),
        'count': len(values)
    }

def fractions(value):
    """
    Convert a float to a fraction.

    Args:
        value (float): The float to convert.

    Returns:
        Fraction: The fraction representation of the float.
    """
    return Fraction(value).limit_denominator()

def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def plot(x, y, kind='line', title=None, xlabel=None, ylabel=None):
    """
    Plot data similar to R's plot() function.

    Args:
        x (list): X-axis data.
        y (list): Y-axis data.
        kind (str): Type of plot ('line', 'scatter', 'bar').
        title (str): Title of the plot.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.

    Returns:
        None
    """
    plt.figure()
    if kind == 'line':
        plt.plot(x, y)
    elif kind == 'scatter':
        plt.scatter(x, y)
    elif kind == 'bar':
        plt.bar(x, y)
    else:
        raise ValueError(f"Plot kind '{kind}' is not supported")
    
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    
    plt.show()