from app.Bubble import Bubble
from app.Insertion import Insertion
from app.Selection import Selection

calc = Bubble()
array = [1, 5, 3, 5, 2, 9, 6, 4, 2]
print(calc.getSorting().sort(array))

calc = Insertion()
array = [4, 2, 6, 4, 9, 7, 5, 3, 7]
print(calc.getSorting().sort(array))

calc = Selection()
array = [3, 8, 5, 3, 6, 8, 9, 2, 1]
print(calc.getSorting().sort(array))