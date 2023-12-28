"""
Author Student ID: A00316036

Description: This module contains functions to perform unit testing using PyTest on the user-defined statistics functions.".
"""

from pytest import main, approx
from analysis_and_visualisation import get_mean, get_median, get_mode, get_range, get_inter_quartile_range, \
    get_standard_deviation, get_mode_skewness, get_median_skewness, get_correlation


def test_get_mean():
    """
    Test the mean function that calculates and returns the mean of a list of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_mean([1, 3, 5, 7, 9]) == 5


def test_get_median_for_odd_list_length():
    """
    Test the median function that calculates and returns the median of a list of values of odd length.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_median([5, 1, 3, 6, 7]) == 5


def test_get_median_for_even_list_length():
    """
    Test the median function that calculates and returns the median of a list of values of even length.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_median([5, 2, 6, 4, 7, 1, 3, 8]) == 4.5


def test_get_mode():
    """
    Test the mode function that calculates and returns the mode of a list of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_mode([5, 1, 3, 9, 3, 3, 4, 7]) == 3


def test_get_range():
    """
    Test the range function that calculates and returns the range of a list of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_range([4, 2, 7, 8, 5]) == 6


def test_inter_quartile_range_for_odd_list_length():
    """
    Test the inter quartile range function that calculates and returns the inter quartile range of a list of values of odd length.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_inter_quartile_range([2, 4, 4, 5, 6, 7, 8]) == 3


def test_inter_quartile_range_for_even_list_length():
    """
    Test the inter quartile range function that calculates and returns the inter quartile range of a list of values of even length.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_inter_quartile_range([1, 3, 3, 4, 5, 6, 6, 7, 8, 8]) == 4


def test_get_standard_deviation():
    """
    Test the standard deviation function that calculates and returns the standard deviation of a list of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_standard_deviation([1, 2, 3, 4, 4, 5]) == approx(1.47, 0.01)


def test_get_mode_skewness():
    """
    Test the mode skewness function that calculates and returns the mode skewness of a list of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_mode_skewness([1, 2, 3, 4, 4, 5]) == approx(-0.567, 0.01)


def test_get_median_skewness():
    """
    Test the median skewness function that calculates and returns the median skewness of a list of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_median_skewness([1, 2, 3, 4, 4, 5]) == approx(-0.68, 0.01)


def test_get_correlation():
    """
    Test the correlation function that calculates and returns the correlation between two lists of values.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError if the result is incorrect.
    """
    assert get_correlation([1, 2, 3, 4], [2, 4, 6, 8]) == approx(1, 0.1)


if __name__ == '__main__':
    main([__file__, '-v'])
