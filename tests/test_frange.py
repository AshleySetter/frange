from frange import frange
import numpy as np
import pytest

"""
These tests test that frange behaviour matches np.arange's 
behaviour, as is desired, such that they can be used iterchangably.
"""

def test_frange_get_array_postiveStepSize():
    """
    Tests that for positive step size frange's returned array matches arange's
    """
    np.testing.assert_allclose(frange(0, 10, 0.1).get_array(), np.arange(0, 10, 0.1), rtol=1e-10)
    return None

def test_frange_get_array_nosteps():
    """
    Tests that for positive step size, with zero steps in interval, 
    frange's returned array matches arange's, which should be empty.
    """
    np.testing.assert_allclose(frange(10, 0, 0.1).get_array(), np.arange(10, 0, 0.1), rtol=1e-10)
    return None
    
def test_frange_get_array_negtaiveStepSize():
    """
    Tests that for negative step size frange's returned array matches arange's
    """
    np.testing.assert_allclose(frange(10, 0, -0.1).get_array(), np.arange(10, 0, -0.1), rtol=1e-10)
    return None

def test_raise_zeroDivisionError():
    """
    Tests that when a zero step size is used frange raises a divide by zero error
    as numpy's arange function does.
    """
    with pytest.raises(ZeroDivisionError):
        t = frange(1, 0, 0)
    return None

def test_frange_get_generator_postiveStepSize():
    """
    Tests that for positive step size frange's returned generator matches arange's
    """
    np.testing.assert_allclose(list(frange(0, 10, 0.1).get_generator()), np.arange(0, 10, 0.1), rtol=1e-10)
    return None

def test_frange_get_generator_nosteps():
    """
    Tests that for positive step size, with zero steps in interval, 
    frange's returned generator matches arange's, which should be empty.
    """
    np.testing.assert_allclose(list(frange(10, 0, 0.1).get_generator()), np.arange(10, 0, 0.1), rtol=1e-10)
    return None
    
def test_frange_get_generator_negtaiveStepSize():
    """
    Tests that for negative step size frange's returned generator matches arange's
    """
    np.testing.assert_allclose(list(frange(10, 0, -0.1).get_generator()), np.arange(10, 0, -0.1), rtol=1e-10)
    return None
    
def test_length():
    assert len(frange(0, 10, 0.1).get_array()) == 100
    return None
