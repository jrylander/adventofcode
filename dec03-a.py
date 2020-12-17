from itertools import islice

with open("dec03-indata.txt") as indata:
    rows = list(indata)
    width = len(rows[0])
    height = len(rows)
    row = col = 0
    trees = 0
    while row < height:
        if rows[row][col % (width-1)] == '#':
            trees += 1 
        row += 1
        col += 3
    print(trees)