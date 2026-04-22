from collections import deque


def parse_grid(grid):
    grid = grid.replace(" ", "").replace("\n", "")
    
    if len(grid) != 81:
        print(" Error: Grid must be 81 characters")
        return None
    
    domains = {}
    for i in range(81):
        if grid[i] == '0':
            domains[i] = list(range(1, 10))
        else:
            domains[i] = [int(grid[i])]
    
    return domains


def get_neighbors():
    neighbors = {i: set() for i in range(81)}
    
    for i in range(81):
        row, col = divmod(i, 9)
        
        for j in range(9):
            neighbors[i].add(row*9 + j)
            neighbors[i].add(j*9 + col)
        
        box_row, box_col = row//3, col//3
        for r in range(box_row*3, box_row*3+3):
            for c in range(box_col*3, box_col*3+3):
                neighbors[i].add(r*9 + c)
        
        neighbors[i].remove(i)
    
    return neighbors

def revise(xi, xj, domains):
    revised = False
    for x in domains[xi][:]:
        if all(x == y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised


def ac3(domains, neighbors):
    queue = deque((xi, xj) for xi in range(81) for xj in neighbors[xi])
    removed = 0
    
    while queue:
        xi, xj = queue.popleft()
        
        if revise(xi, xj, domains):
            removed += 1
            if not domains[xi]:
                return False, removed
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    
    return True, removed

def print_domain_sizes(domains):
    print("\nDomain Size Grid:")
    for i in range(9):
        row = []
        for j in range(9):
            row.append(str(len(domains[i*9 + j])))
        print(" ".join(row))



grid = "000006000059000008200080000045000000003000000006003050000070000000000000000500002"

domains = parse_grid(grid)

if domains:
    neighbors = get_neighbors()
    result, removed = ac3(domains, neighbors)
    
    print("Arc Consistent:", result)
    print("Values Removed:", removed)
    print("Total Arcs = 810+")
    
    print_domain_sizes(domains)
    
    print("\nConclusion:")
    if not result:
        print("A domain became empty -> puzzle unsolvable.")
    else:
        print("No domain is empty -> puzzle is valid.")
        
        solved = all(len(domains[i]) == 1 for i in domains)
        if solved:
            print("All domains reduced to 1 -> solved completely.")
        else:
            print("Not all domains are 1 -> needs backtracking.")