class Helper:
    swaps = 0
    comparisons = 0

    @staticmethod
    def swap_with_counting():
        Helper.swaps += 1

    @staticmethod
    def swap():
        pass

    @staticmethod
    def compare(condition):
        return condition

    @staticmethod
    def compare_with_counting(condition):
        Helper.comparisons += 1
        return condition


def partition(array, key, low, high, swap, compare):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if compare(getattr(array[j], key) <= getattr(pivot, key)):
            i = i + 1
            array[i], array[j] = array[j], array[i]
            swap()
        array[i + 1], array[high] = array[high], array[i + 1]
        swap()
        return i + 1


def quick_sort(array, key, low, high, swap=Helper.swap, compare=Helper.compare):
    if compare(low < high):
        pi = partition(array, key, low, high, swap, compare)
        quick_sort(array, key, low, pi - 1, swap, compare)
        quick_sort(array, key, pi + 1, high, swap, compare)

    return array, Helper


def merge_sort(array, key, swap=Helper.swap, compare=Helper.compare):
    if len(array) > 1:

        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        merge_sort(L, key, swap, compare)
        merge_sort(M, key, swap, compare)

        i = j = k = 0

        while compare(i < len(L)) and compare(j < len(M)):
            if compare(getattr(L[i], key) < getattr(M[j], key)):
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            swap()
            k += 1

        while compare(i < len(L)):
            array[k] = L[i]
            swap()
            i += 1
            k += 1

        while compare(j < len(M)):
            array[k] = M[j]
            swap()
            j += 1
            k += 1
    return array, Helper


def heapify(array, key, n, i, swap, compare):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if compare(l < n) and compare(getattr(array[i], key) < getattr(array[l], key)):
        largest = l

    if compare(r < n) and compare(getattr(array[largest], key) < getattr(array[r], key)):
        largest = r

    if compare(largest != i):
        array[i], array[largest] = array[largest], array[i]
        swap()
        heapify(array, key, n, largest, swap, compare)


def heap_sort(array, key, swap=Helper.swap, compare=Helper.compare):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, key, n, i, swap, compare)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        swap()
        heapify(array, key, i, 0, swap, compare)

    return array, Helper
