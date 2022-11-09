from _CalculadoraSort import Calculadora
from interface.Sort_Impl.SelectionSort import SelectionSort

class Selection(Calculadora):
    def __init__(self):
        self._tipoDeSort = SelectionSort