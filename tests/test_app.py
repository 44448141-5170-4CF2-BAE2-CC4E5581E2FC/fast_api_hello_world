# run with pytest!
import os


def test_important_test_var():
    """Test that the variable "IMPORTANT_TEST_VAR" is set to "important_value".

    (This is just an example test, not actually very useful.)"""
    assert os.environ.get("IMPORTANT_TEST_VAR") == "important_value"
