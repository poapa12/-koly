image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]


def dilatace(image2d):
    rows, cols = len(image2d), len(image2d[0])
    output = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            neighbors = [
                image2d[x][y]
                for x in range(max(0, i-1), min(rows, i+2))
                for y in range(max(0, j-1), min(cols, j+2))
            ]
            output[i][j] = max(neighbors)
 
    return output

def eroze(image2d):
    rows, cols = len(image2d), len(image2d[0])
    output = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            neighbors = [
                image2d[x][y]
                for x in range(max(0, i-1), min(rows, i+2))
                for y in range(max(0, j-1), min(cols, j+2))
            ]
            output[i][j] = min(neighbors)

    return output


def print_table(matrix, title):
    print(f"\n{title}:")
    cols = len(matrix[0])
    
    print("| " + " | ".join(map(str, range(cols))) + " |")
    print("|-" + "-|-".join(["-" * len(str(i)) for i in range(cols)]) + "-|")
    
    for row in matrix:
        print("| " + " | ".join(map(str, row)) + " |")

print_table(image2d, "Původní tabulka")

dilated = dilatace(image2d)
print_table(dilated, "Po dilataci")

eroded = eroze(image2d)
print_table(eroded, "Po erozi")
