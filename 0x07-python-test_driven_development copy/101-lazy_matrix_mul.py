#!/usr/bin/python3
"""
This module defines the lazy_matrix_mul function that
multiplies two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int or float): The first matrix.
        m_b (list of lists of int or float): The second matrix.

    Returns:
        list of lists of int or float: The product of the two matrices.

    Raises:
        ValueError: If m_a or m_b is empty (it means: = [] or = [[]]),
        or if m_a and m_b cannot be multiplied.
    """
    if m_a == [] or m_b == []:
        raise ValueError('m_a can\'t be empty or m_b can\'t be empty')
    try:
        result = np.dot(m_a, m_b).tolist()
    except ValueError:
        raise ValueError('m_a and m_b can\'t be multiplied')
    return result
