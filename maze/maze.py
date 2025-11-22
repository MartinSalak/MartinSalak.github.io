from browser import document, html, bind

GRID_SIZE = 16

# Starting position
x, y = 0, 0

grid = document["grid"]
cells = []

# Create 16x16 grid
for i in range(GRID_SIZE * GRID_SIZE):
    cell = html.DIV(Class="cell")
    grid <= cell
    cells.append(cell)

# Keep track of visited cells
visited = set()
visited.add((x, y))

def update_highlight():
    for i, cell in enumerate(cells):
        row = i // GRID_SIZE
        col = i % GRID_SIZE
        if (col, row) == (x, y):
            cell.attrs["class"] = "cell active"
        elif (col, row) in visited:
            cell.attrs["class"] = "cell visited"
        else:
            cell.attrs["class"] = "cell"

update_highlight()

@bind(document, "keydown")
def move_square(event):
    global x, y
    key = event.key
    if key == "ArrowUp" and y > 0:
        y -= 1
    elif key == "ArrowDown" and y < GRID_SIZE - 1:
        y += 1
    elif key == "ArrowLeft" and x > 0:
        x -= 1
    elif key == "ArrowRight" and x < GRID_SIZE - 1:
        x += 1

    visited.add((x, y))
    update_highlight()
