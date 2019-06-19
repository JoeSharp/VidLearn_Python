import time
from random import randint
from typing import List, Callable

from CORE_TheoryOfComputation.Benchmark.TickPrinter import TickPrinter
from CORE_Algorithms.Searching.linear_search import linear_search
from CORE_Algorithms.Searching.binary_search import binary_search
from CORE_Algorithms.Searching.binary_tree_search import binary_tree_search
from CORE_Algorithms.Searching.common import SearchFunction
from CORE_Algorithms.Sorting.common import primitive_compare


def generate_benchmark_csv(filename: str,
                           list_size_range: range,
                           tick: Callable[[], None]) -> None:
    """
    Run timed searching algorithms, outputting results to a CSV.
    :param filename: The filename to write the CSV to
    :param list_size_range: The range of list sizes to use
    :param tick: A function to receive keep alive ticks from the process after every sort
    :return: None
    """
    search_functions: List[SearchFunction] = [linear_search, binary_search, binary_tree_search]

    # Open the file
    with open(filename, 'w') as f:
        # Write the CSV header
        f.write("Count,{}\n".format(",".join([s.__name__ for s in search_functions])))

        # For each list size in the given range
        for list_size in list_size_range:
            # Generate a random list of numbers, same list for both sort functions
            the_list: List[int] = [randint(0, 1000) for x in range(list_size)]
            times_taken: List[float] = []

            # For each sort function, take time at start, subtract from time at end
            for search_function in search_functions:
                start_time = time.process_time_ns()
                search_function(the_list,
                                the_list[len(the_list) - 1],
                                primitive_compare,
                                primitive_compare)
                times_taken.append(time.process_time_ns() - start_time)
                tick()

            # Write entry into the CSV
            f.write("{},{}\n".format(list_size,",".join([str(f) for f in times_taken])))


tick_printer: TickPrinter = TickPrinter()
generate_benchmark_csv('searching_benchmark.csv', range(10, 3000, 100), lambda: tick_printer.tick())
