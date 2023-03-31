import csv
import time
from random import shuffle

from src.entity.student import Student
from src.services.sort import quick_sort, Helper, merge_sort, heap_sort


def prepare_data(to_shuffle: bool = False) -> list[Student]:
    reader = csv.DictReader
    data = Student.read_from_stream(filename='data/students_data.csv', reader=reader)
    if to_shuffle:
        shuffle(data)
    return data


def make_timer(callback, *args):
    start = time.perf_counter_ns()
    array, helper = callback(*args)
    end = time.perf_counter_ns()
    print(f"{callback.__name__}: Spent time {end - start} nanoseconds")
    print(f"number of comparisons: {helper.comparisons}, number of swaps: {helper.swaps}\n")
    helper.swaps, helper.comparisons = 0, 0
    return array


if __name__ == '__main__':
    students = prepare_data(True)
    key = 'firstname'
    # Сортировка для неотсортированного массива и для отсортированного
    sorted_students = make_timer(quick_sort, students.copy(), key, 0, len(students) - 1, Helper.swap_with_counting,
                                 Helper.compare_with_counting)
    make_timer(quick_sort, sorted_students, key, 0, len(students) - 1, Helper.swap_with_counting,
               Helper.compare_with_counting)

    make_timer(merge_sort, students.copy(), key, Helper.swap_with_counting, Helper.compare_with_counting)
    make_timer(merge_sort, sorted_students, key, Helper.swap_with_counting, Helper.compare_with_counting)

    make_timer(heap_sort, students.copy(), key, Helper.swap_with_counting, Helper.compare_with_counting)
    res = make_timer(heap_sort, sorted_students, key, Helper.swap_with_counting, Helper.compare_with_counting)

    Student.write_in_stream(res, csv.DictWriter, 'data/sorted_student.csv')
