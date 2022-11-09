from app.Bubble import Bubble
from app.Insertion import Insertion
from app.Selection import Selection

def test_bubble_working():
    calc = Bubble()
    array = calc.getSorting().sort([5, 4, 3, 3, 2, 1])


    assert array == [1, 2, 3, 3, 4, 5]

def test_insertion_working():
    calc = Insertion()
    array = calc.getSorting().sort([5, 4, 3, 3, 2, 1])


    assert array == [1, 2, 3, 3, 4, 5]

def test_bubble_working():
    calc = Selection()
    array = calc.getSorting().sort([5, 4, 3, 3, 2, 1])


    assert array == [1, 2, 3, 3, 4, 5]