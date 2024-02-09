
from app.sum import add_number




def test_add_number():
    
    assert add_number(1, 2) == 4
    assert add_number(-1, 1) == 0
    assert add_number(0, 0) == 0
    assert add_number(10, -5) == 5