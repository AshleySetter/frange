[![Build Status](https://travis-ci.org/AshleySetter/frange.png)](https://travis-ci.org/AshleySetter/frange)
[![codecov](https://codecov.io/gh/AshleySetter/frange/branch/master/graph/badge.svg)](https://codecov.io/gh/AshleySetter/frange)
[![Documentation Status](https://readthedocs.org/projects/frange/badge/?version=latest)](http://frange.readthedocs.org/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/frange.svg)](https://badge.fury.io/py/frange)

# frange
Data type for efficiently storing large arrays of equally separated data in python, similar to range but for floats.

This is a simple package containing a class which can be used in a similar manner to the built-in range function in python. It can be used to create a generator or a numpy array containing the desired, equally seperated, values.

It generates numbers in the same manner as numpy's arange function.

## Example usage

```python
# you can create an frange object like so
>>> time = frange(0, 2, 1e-3)

# you can print the length of the array it will generate
>>> printlen(time) # prints length of frange, just like an array or list

# you can create a generator
>>> generator = time.get_generator() # gets a generator instance
>>> for i in generator: # iterates through printing each element
>>>     print(i)

# you can create a numpy array
>>> array = time.get_array() # gets an array instance
>>> newarray = 5 * array # multiplies array by 5

# you can also get the start, stop and step by accessing the slice parameters
>>> start = time.slice.start
>>> stop = time.slice.stop
>>> step = time.slice.step
```
