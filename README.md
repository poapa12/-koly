# Dilance a Eroze v 2D poli

## Popis projektu
Je dáno dvourozměrné pole `image2d` o rozměrech **9x9**. Hodnoty matice jsou v rozsahu **0 - 4**. Ve středu matice je hodnota **4**, směrem k okrajům se hodnoty budou snižovat až na **0**. Kódy pro inicializaci jsou uvedeny níže.

### Použitý jazyk
 - Python
 - Markdown
## Generování matice 

```python
image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]
```
**Výchozí podoba matice**

```
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 1, 1, 0]
[0, 1, 2, 2, 2, 2, 2, 1, 0]
[0, 1, 2, 3, 3, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 3, 3, 2, 1, 0]
[0, 1, 2, 2, 2, 2, 2, 1, 0]
[0, 1, 1, 1, 1, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
```
## Převod hodnot z matice do markdown tabulky

```python
print("| " + " | ".join(map(str, range(9))) + " |")
print("|-" + "-|-".join(["-" * len(str(i)) for i in range(9)]) + "-|")
for row in image2d:
    print("| " + " | ".join(map(str, row)) + " |")
```
**Výchozí podoba tabulky**

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 3 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 4 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 3 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Implementace funkcí
### Dilatace
Každý prvek matice se nahradí maximální hodnotou z původních sousedních hodnot (vlevo, vpravo, nad a pod).
```python
def dilatace(image2d):
    """ Provádí morfologickou dilataci na dvourozměrném poli. """
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
```
**Výchozí podoba tabulky**
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 |
| 1 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 4 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 4 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 4 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 1 |
| 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### Eroze
Každý prvek matice se nahradí minimální hodnotou z původních sousedních hodnot (vlevo, vpravo, nad a pod).
```python
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
```
**Výchozí podoba tabulky**
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 2 | 2 | 2 | 1 | 0 | 0 |
| 0 | 0 | 1 | 2 | 3 | 2 | 1 | 0 | 0 |
| 0 | 0 | 1 | 2 | 2 | 2 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
