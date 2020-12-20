from itertools import islice

with open("dec03-indata.txt") as indata:
    rows = list(indata)
    width = len(rows[0])
    height = len(rows)
    treesProd = 1
    for (dx, dy) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        trees = 0
        row = col = 0
        while row < height:
            if rows[row][col % (width-1)] == '#':
                trees += 1 
            row += dy
            col += dx
        treesProd *= trees
    print(treesProd)