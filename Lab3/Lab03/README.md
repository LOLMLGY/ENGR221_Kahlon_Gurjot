# ENGR 221 Lab 3: Sorting Algorithms

A pygame visualizer that sorts carrots by length using Selection, Insertion,
and Bubble sort.

Files
sorting_algorithms.py: It stores te array to sort and implemnt all the sort types along with get_runtime()
Yes the file was edited with comments and added insertion and bubble sort.

controller.py: Controls the main loop and keyboard inputs along with timings. Not edited

display.py: Responsible for drawing the array and highlighting the carrots. Not edited

preferences.py: The storage for many of the constants used in the program.(Sizing, colors, image paths)

images fodler: holds the images for carrots. Not edited

answers.txt: Answers for lab. Very edited and new file...

How to run
1. Do `pip install pygame` if you dont have it.
2. From the `Lab3` folder run: `python controller.py`
3. Controls: "s" for selection, "i" for insertion, "b" for bubble, "r" for reset,
   "Right arrow button" (or L) for advance one step, "Spacebar" toggle continuous advance.

Also running the file 'sorting_algorithims.py" can let you check the runtimes of the sorts on your device with any length of list. Just change the s.restart("bubble") Have "bubbles" as "insertion", "selection", or "bubble" for each sorting algorithim. 
