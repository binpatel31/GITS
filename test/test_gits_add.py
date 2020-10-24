import argparse
import sys
import os

sys.path.insert(1, os.getcwd())

from gits_add import gits_add_func
from mock import patch


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names=["test1", "test2"]))
@patch("subprocess.Popen", return_value="anything")
def test_gits_add_func_1(mock_var1, mock_args):
    """
    Function to test gits_add, success case
    """
    mock_args = parse_args(mock_args)
    test_result = gits_add_func(mock_args)
    assert True == test_result, "Normal case"
