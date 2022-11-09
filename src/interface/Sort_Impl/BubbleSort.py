from interface.SortStrategy import ListOrderingStrategy

class BubbleSort(ListOrderingStrategy):
    def sort(array):
        indexing_length = len(array) - 1
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, indexing_length):
                if(array[i] > array[i+1]):
                    sorted = False
                    array[i], array[i+1] = array[i+1], array[i]
            
        return array