"""Tiny app the demo receipts measure against."""


def add(a, b):
    return a + b


def percent_change(old, new):
    if old == 0:
        raise ValueError("old must be nonzero")
    return (new - old) / old * 100
