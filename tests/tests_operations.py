from src.main import add,sub

def test_add():
    assert add(5,3)==8
    assert add(2,3)==5

def test_sub():
    assert sub(5,1)==4
    assert sub(4,3)==1
    assert sub(2,3)==-1


