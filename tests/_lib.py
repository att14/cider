# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def threshold_comparator(threshold):
    def comparator(actual, expected):
        if isinstance(actual, float) and isinstance(expected, float):
            return abs(actual - expected) <= threshold
        else:
            return actual == expected

    return comparator


def assert_called_with_comparator(mock_self, comparator, *args, **kwargs):
    _, actual_args, actual_kwargs = mock_self.mock_calls[-1]

    for actual, expected in zip(actual_args, args):
        assert comparator(actual, expected)

    for key, expected in kwargs.items():
        assert comparator(actual_kwargs.get(key), expected)


def assert_called_with_threshold(mock_self, threshold, *args, **kwargs):
    assert_called_with_comparator(
        mock_self,
        threshold_comparator(threshold),
        *args,
        **kwargs
    )
