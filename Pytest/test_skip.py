import pytest
import sys
@pytest.mark.skip(reason="not included in this build")
def test_demo_1():
    assert True
@pytest.mark.skipif(sys.version_info<(4,6),reason="requires python 4.6 or higher")
def test_demo_2():
    assert True

def test_demo_3():
    assert True