import unittest
from typing import List, Optional
from random import randint
from CORE_Algorithms.Sorting.bubble_sort import bubble_sort
from CORE_Algorithms.Sorting.merge_sort import merge_sort
from CORE_Algorithms.Sorting.insertion_sort import insertion_sort
from CORE_Algorithms.Sorting.quick_sort import quick_sort
from CORE_Algorithms.Sorting.common import SortFunction, primitive_compare, primitive_reverse_compare
from CORE_Algorithms.Sorting.Person import Person, compare_name, compare_age


class TestSortFunctions(unittest.TestCase):
    __sort_functions: List[SortFunction] = [quick_sort, insertion_sort, bubble_sort, merge_sort]

    def test_numbers(self):
        for sort_function in self.__sort_functions:
            my_list: List[int] = [4, 5, 3, 1, 9, 8]
            my_sorted_list: List[int] = sort_function(my_list, primitive_compare)
            my_reversed_list: List[int] = sort_function(my_list, primitive_reverse_compare)
    
            print("Integers: {}\nInput: {}\nSorted: {}\nReversed: {}".format(
                sort_function.__name__, my_list, my_sorted_list, my_reversed_list))
            self.assertEqual([1, 3, 4, 5, 8, 9], my_sorted_list)
            self.assertEqual([9, 8, 5, 4, 3, 1], my_reversed_list)

    def test_empty_list(self):
        for sort_function in self.__sort_functions:
            my_list: List = []
            sorted_list = sort_function(my_list, lambda x, y: x < y)
            self.assertEqual([], sorted_list)

    def test_mixed_types(self):
        for sort_function in self.__sort_functions:
            my_list: List = [1, 2, 'joe', 'foobar']
            with self.assertRaises(Exception) as context:
                sort_function(my_list, lambda x, y: x < y)

            self.assertTrue('not supported between instances' in str(context.exception))

    def test_string(self):
        for sort_function in self.__sort_functions:
            my_list: List[str] = ["Bravo", "Delta", "Charlie", "Alpha", "Echo", "Sierra", "Foxtrot"]
            my_sorted_list: List[str] = sort_function(my_list, primitive_compare)
            my_reversed_list: List[str] = sort_function(my_list, primitive_reverse_compare)
            print("Strings: {}\nInput: {}\nSorted: {}\nReversed: {}".format(
                sort_function.__name__, my_list, my_sorted_list, my_reversed_list))
            self.assertEqual(
                ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Sierra"],
                my_sorted_list)
            self.assertEqual(
                ["Sierra", "Foxtrot", "Echo", "Delta", "Charlie", "Bravo", "Alpha"],
                my_reversed_list)

    def test_random(self):
        for sort_function in self.__sort_functions:
            my_list: List[int] = [randint(0, 100) for i in range(100)]
            my_sorted_list: List[int] = sort_function(my_list, primitive_compare)

            print("Random Numbers: {}\nInput: {}\nSorted: {}".format(
                sort_function.__name__, my_list, my_sorted_list))

            last: Optional[int] = None
            num_checks: int = 0
            for s in my_sorted_list:
                if last is not None:
                    num_checks += 1
                    self.assertTrue(last <= s)
                last = s
            self.assertEqual(num_checks, len(my_list) - 1)

    def test_objects(self):
        for sort_function in self.__sort_functions:
            my_list: List[Person] = [
                Person("Frodo", 55),
                Person("Sam", 35),
                Person("Bilbo", 111),
                Person("Sauron", 3000),
                Person("Gollum", 500)
            ]
            by_name: List[Person] = sort_function(my_list, compare_name)
            by_age: List[Person] = sort_function(my_list, compare_age)

            by_name_names = [x.get_name() for x in by_name]
            by_age_names = [x.get_name() for x in by_age]

            print("Objects: {}\nInput: {}\nBy Name: {}\nBy Age: {}".format(
                sort_function.__name__, my_list, by_name, by_age))
            self.assertEqual(["Bilbo", "Frodo", "Gollum", "Sam", "Sauron"], by_name_names)
            self.assertEqual(["Sam", "Frodo", "Bilbo", "Gollum", "Sauron"], by_age_names)

