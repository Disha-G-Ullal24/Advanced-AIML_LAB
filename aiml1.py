# Grid Legend: O = Obstacle, T = Task, ' ' = Empty
grid = [
    [' ', ' ', ' ', 'T', ' '],
    ['T', 'O', ' ', ' ', ' '],
    [' ', ' ', ' ', 'O', 'T'],
    ['O', ' ', ' ', ' ', ' '],
    [' ', 'T', 'O', ' ', ' ']
]

agent = [0, 0]  # Starting position (row, col)

def show():
    print("  +" + "---+"*len(grid[0]))
    for r in range(len(grid)):
        row = "|"
        for c in range(len(grid[0])):
            cell = "A" if [r,c]==agent else grid[r][c]
            row += f" {cell} |"
        print(r, row)   # show row index
        print("  +" + "---+"*len(grid[0]))
    print("    " + "   ".join(str(c) for c in range(len(grid[0]))))  # column index
    print()

def move():
    r, c = agent
    if grid[r][c] == 'T':          # Do task if present
        print("Task done at", (r,c))
        grid[r][c] = ' '
        return
    # Priority moves: Right, Down, Left, Up
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr, nc = r+dr, c+dc
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]!="O":
            agent[:] = [nr,nc]
            print("Agent moved to", (nr,nc))
            return
    print("No move possible")

for step in range(15):
    print("Step", step+1)
    show()
    move()
