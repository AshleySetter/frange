from frange import frange
import numpy as np
import pytest

def test_frange():
    """
    Test that frange behaviour matches np.arange's behaviour.
    """
    np.testing.assert_allclose(frange(0, 10, 0.1).get_array(), np.arange(0, 10, 0.1), rtol=1e-10)

    np.testing.assert_allclose(frange(10, 0, 0.1).get_array(), np.arange(10, 0, 0.1), rtol=1e-10)

    np.testing.assert_allclose(frange(10, 0, -0.1).get_array(), np.arange(10, 0, -0.1), rtol=1e-10)

    with pytest.raises(ZeroDivisionError):
        t = frange(1, 0, 0)

    
    return None
