# Conway's Game of Life
import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list of lists for cells
nextCells = []

for x in range(WIDTH):
    column = [] # Create a new column
    