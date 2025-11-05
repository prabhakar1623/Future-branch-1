import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(6, 4) == 2
