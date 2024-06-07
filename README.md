
# r_like

A Python library mimicking some of R's functionality, including functions for statistical calculations, sequence generation, and fraction representation.

## Installation

To install the library, clone the repository and run:

```sh
pip install .
```

## Usage

```python
from r_like import r_like

# Example usage
print(r_like.choose(52, 5))  # Should output 2598960

# Using the seq function
print(r_like.seq(1, 10))  # Should output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculating mean
print(r_like.mean([1, 2, 3, 4, 5]))  # Should output 3.0

# Calculating standard deviation
print(r_like.sd([1, 2, 3, 4, 5]))  # Should output 1.5811388300841898

# Getting summary statistics
print(r_like.summary([1, 2, 3, 4, 5]))
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
print(r_like.fractions(0.5))  # Should output Fraction(1, 2)
```

## Running Tests

To run the tests, use:

```sh
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.
