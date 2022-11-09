import sys
sys.path.append("./app")

from interface.Sort_Impl.BubbleSort import BubbleSort
from _CalculadoraSort import Calculadora

class Bubble(Calculadora):

    def __init__(self):
        self._tipoDeSort = BubbleSort