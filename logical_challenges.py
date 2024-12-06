def next_player(n) :
    if n == 1 :
        return 0
    return 1

def empty_grid() :
    grid = []
    for i in range(3) :
        l = []
        for j in range(3) :
            l.append(" ")
        grid.append(l)
    return grid