# Simple Python program to read an ASCII grid,
# find the start 'S' and list all task cells 'T'

grid = [
    [' ', ' ', 'O', 'T', ' '],
    ['T', 'O', ' ', ' ', ' '],
    [' ', 'S', ' ', 'O', 'T'],
    ['O', ' ', ' ', ' ', ' '],
    [' ', 'T', ' ', ' ', ' ']
]

start = None
tasks = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'T':
            tasks.append((i, j))

print("Start Position:", start)
print("Task Cells:", tasks)
