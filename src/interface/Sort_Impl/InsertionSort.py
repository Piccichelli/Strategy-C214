from interface.SortStrategy import ListOrderingStrategy

class InsertionSort(ListOrderingStrategy):
    def sort(array):
        indexing_length = range(1, len(array))

        for i in indexing_length:
            value_to_sort = array[i]

            while array[i-1] > value_to_sort and i>0:
                array[i], array[i-1] = array[i-1], array[i]
                i = i - 1
        
        return array