from interface.SortStrategy import ListOrderingStrategy

class SelectionSort(ListOrderingStrategy):
    def sort(array):
        indexing_length = range(0, len(array)-1)

        for i in indexing_length:
            min_value = i

            for j in range (i+1, len(array)):
                if array[j] < array[min_value]:
                    min_value = j

            if min_value != i:
                array[min_value], array[i] = array[i], array[min_value]
        
        return array