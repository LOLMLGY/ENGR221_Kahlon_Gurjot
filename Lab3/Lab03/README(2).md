# ENGR 221 - Lab 3: Sorting Algorithms

A pygame visualizer that sorts carrots by length using Selection, Insertion,
and Bubble sort.

## Files
| File | Description | Modified? |
|------|-------------|-----------|
| `sorting_algorithms.py` | Stores the array to sort and implements `selection_sort()`, `insertion_sort()`, `bubble_sort()` as generators, plus `get_runtime()`. | **Yes** (commented selection sort; implemented insertion and bubble sort; added header and docstrings) |
| `controller.py` | Main loop and keyboard handling. | No |
| `display.py` | Draws the array and highlighted carrots. | No |
| `preferences.py` | Constants (sizes, colors, image paths). | No |
| `images/` | Carrot images used for the bars. | No |
| `answers.txt` | Written answers for Parts 1-5. | New |

## How to run
1. Install pygame: `pip install pygame`
2. From the `Lab3` folder run: `python controller.py`
3. Controls: **S** selection, **I** insertion, **B** bubble, **R** reset,
   **Right arrow** (or L) advance one step, **Space** toggle continuous advance.

## Timing the algorithms
In the `if __name__ == "__main__":` block of `sorting_algorithms.py`, change
`s.restart("selection", 100)` to `"insertion"` or `"bubble"` and/or a different
length, then run `python sorting_algorithms.py`.
