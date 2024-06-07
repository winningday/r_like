
# r_like

A Python library mimicking some of R's functionality, including functions for statistical calculations, sequence generation, and fraction representation.

## Installation

To install the library, clone the repository and run:

```sh
pip install .
```

## Usage

You can import the functions in two ways:

## Method 1: Import Individual Functions

```python
from r_like import (
    choose, seq, mean, median, sd, var, sum_values, prod, 
    summary, fractions, factorial, plot, one_in
)

# Example usage
print(choose(52, 5))  # Should output 2598960

# Using the seq function
print(seq(1, 10))  # Should output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculating mean
print(mean([1, 2, 3, 4, 5]))  # Should output 3.0

# Calculating standard deviation
print(sd([1, 2, 3, 4, 5]))  # Should output 1.5811388300841898

# Getting summary statistics
print(summary([1, 2, 3, 4, 5]))
# Should output:
# {
#     'min': 1,
#     'max': 5,
#     'mean': 3.0,
#     'median': 3,
#     'sd': 1.5811388300841898,
#     'var': 2.5,
#     'sum': 15,
#     'prod': 120,
#     'count': 5
# }

# Converting a float to fraction
print(fractions(0.5))  # Should output Fraction(1, 2)

# Calculating factorial
print(factorial(5))  # Should output 120

# Plotting example
x = seq(1, 10)
y = [i**2 for i in x]
plot(x, y, kind='line', title='Example Plot', xlabel='X-axis', ylabel='Y-axis')

# Using the one_in function
print(one_in(47/85))  # Should output "approximately 1 in 2"
print(one_in(33/16660))  # Should output "approximately 1 in 505"

```

## Method 2: Import the Entire Module
```python
import r_like as rl

# Example usage
print(rl.choose(52, 5))  # Should output 2598960

# Using the seq function
print(rl.seq(1, 10))  # Should output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculating mean
print(rl.mean([1, 2, 3, 4, 5]))  # Should output 3.0

# Calculating standard deviation
print(rl.sd([1, 2, 3, 4, 5]))  # Should output 1.5811388300841898

# Getting summary statistics
print(rl.summary([1, 2, 3, 4, 5]))
# Should output:
# {
#     'min': 1,
#     'max': 5,
#     'mean': 3.0,
#     'median': 3,
#     'sd': 1.5811388300841898,
#     'var': 2.5,
#     'sum': 15,
#     'prod': 120,
#     'count': 5
# }

# Converting a float to fraction
print(rl.fractions(0.5))  # Should output Fraction(1, 2)

# Calculating factorial
print(rl.factorial(5))  # Should output 120

# Plotting example
x = rl.seq(1, 10)
y = [i**2 for i in x]
rl.plot(x, y, kind='line', title='Example Plot', xlabel='X-axis', ylabel='Y-axis')

# Using the one_in function
print(rl.one_in(47/85))  # Should output "approximately 1 in 2"
print(rl.one_in(33/16660))  # Should output "approximately 1 in 505"

```


## Running Tests

To run the tests, use:

```sh
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.
