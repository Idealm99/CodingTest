def solution(park, routes):
    directions = {'S': (1, 0), 'N': (-1, 0), 'E': (0, 1), 'W': (0, -1)}
    
    # Find starting position
    for i, row in enumerate(park):
        if 'S' in row:
            start = [i, row.index('S')]
            break
    
    current = start.copy()
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        
        dx, dy = directions[direction]
        new_position = current.copy()
        
        for _ in range(distance):
            new_x, new_y = new_position[0] + dx, new_position[1] + dy
            
            if (0 <= new_x < len(park) and 
                0 <= new_y < len(park[0]) and 
                park[new_x][new_y] != 'X'):
                new_position = [new_x, new_y]
            else:
                new_position = current.copy()
                break
        
        current = new_position
    
    return current