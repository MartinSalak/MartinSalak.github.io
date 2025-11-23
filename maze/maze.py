from browser import document, html, bind

GRID_SIZE = 16

grid = document["grid"]
cells = []

# Simple maze layout (0 = empty, 1 = wall)
# You can edit these however you want!
MAZE = [
    "0000010000000000",
    "0111010111110110",
    "0100010000010010",
    "0101110111011110",
    "0101000100010000",
    "0101111101110110",
    "0000000001000010",
    "0111111101111010",
    "0100000100000010",
    "0101110111111010",
    "0100010000001010",
    "0111010111101110",
    "0001010000100000",
    "0111011100111110",
    "0000000000000002",
    "0111111111111111"
]
# '2' means **goal**

# Player starting position
x, y = 0, 0
visited = set()
visited.add((x, y))


# Create grid cells
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        cell = html.DIV(Class="cell")
        cells.append(cell)
        grid <= cell


def update_grid():
    for i, cell in enumerate(cells):
        row = i // GRID_SIZE
        col = i % GRID_SIZE
        tile = MAZE[row][col]

        # Reset
        cell.attrs["class"] = "cell"

        # Wall
        if tile == "1":
            cell.attrs["class"] += " wall"

        # Goal
        elif tile == "2":
            cell.attrs["class"] += " goal"

        # Visited path
        if (col, row) in visited and tile != "2":
            cell.attrs["class"] += " visited"

        # Player
        if (col, row) == (x, y):
            cell.attrs["class"] += " active"


update_grid()


@bind(document, "keydown")
def move(event):
    global x, y

    dx = dy = 0
    if event.key == "ArrowUp":
        dy = -1
    elif event.key == "ArrowDown":
        dy = 1
    elif event.key == "ArrowLeft":
        dx = -1
    elif event.key == "ArrowRight":
        dx = 1
    else:
        return

    new_x = x + dx
    new_y = y + dy

    # Stay within bounds
    if not (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE):
        return

    # Check wall
    if MAZE[new_y][new_x] == "1":
        return

    # Move player
    x, y = new_x, new_y
    visited.add((x, y))

    update_grid()

    # Check goal
    if MAZE[y][x] == "2":
        alert("🎉 You reached the goal!")


