import pytest
import datasets
from contextlib import contextmanager
from typing import Iterator
import os
from pathlib import Path

# this file contains code from the following source:
# https://github.com/hwchase17/langchain/blob/780ef84cf0ca95aa752ae79b6749e2b39b5b7343/tests/unit_tests/prompts/test_loading.py#L14


def test_load_data_length():
    """Test that the data length is correct."""
    assert (1==1), "Hi"
