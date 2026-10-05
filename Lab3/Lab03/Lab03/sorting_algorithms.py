"""
Author: Gurjot Kahlon
last updated: october 5th, 2026
description: contains the sortingalgorithms class for the engr 221 lab 3
sorting visualizer (carrots sorted by length). the class stores the array
to be sorted and implements three in-place sorting algorithms as generator
functions: selection sort, insertion sort, and bubble sort. each algorithm
"yields" a pair of indices at every step so the gui can highlight the
carrots being examined. the get_runtime() method times how long an
algorithm takes to finish on a randomly generated list.
"""

import random
import time

from preferences import Preferences

class sortingalgorithms:
    def __init__(self):
        # the algorithm to sort
        self.array = []

        # any indices to highlight
        self.inner_idx = -1
        self.outer_idx = -1 

        # a string representing the current sorting algorithm
        self.current_alg = None

        # store the method of the sorting algorithm being run
        self.alg_method = None
    
    def create_new_array(self, length=Preferences.NUM_ELEMENTS) -> list:
        """ create a new array to sort """
        return [random.randint(0, Preferences.MAX_VAL) \
                      for _ in range(length)]
    
    def get_next_step(self) -> None:
        """ updates the value of self.selected_idx whenever we reach 
            a "yield" statement in any of the below sorting algorithms. """
        
        try:
            # treats the current sorting algorithm as an iterator
            # and sets self.selected_idx to be the next "element"
            self.outer_idx, self.inner_idx = next(self.alg_method)
        # clear the selected_idx value when we reach the end of the method
        except StopIteration:
            self.outer_idx, self.inner_idx = -1, -1

    def restart(self, new_alg, length=Preferences.NUM_ELEMENTS) -> None:
        """ restart the sorting process with the new algorithm. 
            creates a new array to sort. """
        
        self.current_alg = new_alg
        self.alg_method = {
            "selection" : self.selection_sort,
            "insertion" : self.insertion_sort,
            "bubble" : self.bubble_sort
        }[self.current_alg]()
        self.array = self.create_new_array(length)
        self.outer_idx, self.inner_idx = -1, -1

    def selection_sort(self):
        """ an implementation of the selection sorth algorithm. 
            a generator function which creates an iterator that 
            iterates through each "yielded" value. """
        
        # number of items in the list
        n = len(self.array)

        # position i is the first slot of the still-unsorted portion;
        # everything before index i is already in its final place
        for i in range(n):
            # highlight the slot we are about to fill
            yield -1, i
            # assume the smallest remaining item is at position i
            min_idx = i

            # scan the rest of the unsorted portion for something smaller
            for j in range(i + 1, n):
                # highlight the current minimum and the item being compared
                yield min_idx, j

                # found a new smallest item, so remember where it is
                if self.array[j] < self.array[min_idx]:
                    min_idx = j 
            
            # swap the smallest remaining item into position i
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            # show the result of the swap
            yield i, min_idx
                

    def insertion_sort(self):
        """ an implementation of the insertion sort algorithm. 
            sorts self.array in place (no new list is created). 
            a generator function which yields (outer_idx, inner_idx) 
            after every comparison/swap so the gui can display each step. """

        n = len(self.array)

        # everything left of index i is sorted; we "insert" the item at 
        # index i into its correct place within that sorted portion
        for i in range(n):
            # j tracks where the item being inserted currently sits
            j = i
            # highlight the item we are about to insert
            yield i, j

            # move the item left while it is smaller than its left neighbor
            while j > 0 and self.array[j - 1] > self.array[j]:
                # swap the item with its left neighbor
                self.array[j - 1], self.array[j] = self.array[j], self.array[j - 1]
                # the item is now one position to the left
                j -= 1
                # show the state after this swap
                yield i, j


    def bubble_sort(self):
        """ an implementation of the (slightly optimized) bubble sort 
            algorithm. sorts self.array in place (no new list is created). 
            a generator function which yields (outer_idx, inner_idx) 
            for each pair of neighbors that is compared. """

        n = len(self.array)

        # each pass "bubbles" the largest remaining item to the right end
        for i in range(n - 1):
            # the last i items are already sorted, so skip them
            for j in range(n - 1 - i):
                # highlight the two neighbors being compared
                yield j, j + 1

                # if neighbors are out of order, swap them
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    # show the result of the swap
                    yield j, j + 1

    def get_runtime(self) -> float:
        """ returns the length of time (in seconds) that it took for 
            the function_to_run to sort a list of length list_length """

        # get the time before running
        start_time = time.time()
        # sort the given list
        for _ in self.alg_method:
            pass
        # get the time after running
        end_time = time.time()
        # return the difference
        return end_time - start_time

if __name__ == "__main__":
    s = sortingalgorithms()
    s.restart("bubble", 10000)
    print(s.get_runtime())