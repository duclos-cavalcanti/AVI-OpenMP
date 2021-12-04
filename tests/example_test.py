import pytest

def foo(i):
    return i;

def test_foo():
    """Description
    
    @param param:  Description
    @type  param:  Type
    
    @return:  Description
    """
    assert foo(1) == 1, "foo is not equal to 1"
    return

def test_foo_wrong():
    """Description
    
    @param param:  Description
    @type  param:  Type
    
    @return:  Description
    """
    assert foo(2) == 1, "foo is not equal to 1"
    return
