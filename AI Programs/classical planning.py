def a_star(start, goal, neighbors, h):
    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: h(start, goal)}

    while open_set:
        open_set.sort(key=lambda id: f_score.get(id, float('inf')))
        current = open_set.pop(0)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, d in neighbors(current):
            tentative_g_score = g_score.get(current, float('inf')) + d
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append(neighbor)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path

def neighbors(id):
    linkage_map = {
        1: [(2, 1.5), (3, 1.5)],
        2: [(1, 1.5), (4, 3.0)],
        3: [(1, 1.5), (5, 4.5)],
        4: [(2, 3.0), (5, 2.0), (6, 2.5)],
        5: [(3, 4.5), (4, 2.0), (6, 2.5)],
        6: [(4, 2.5), (5, 2.5)],
    }
    return linkage_map[id]

def position(id):
    position_map = {
        1: (0, 0),
        2: (1, 2),
        3: (2, -1),
        4: (4, 2),
        5: (4, 0),
        6: (6, 1),
    }
    return position_map[id]

def heuristic(node, goal):
    return abs(position(node)[0] - position(goal)[0]) + abs(position(node)[1] - position(goal)[1])

if __name__ == '__main__':
    path = a_star(1, 6, neighbors, heuristic)
    print('Path:', path)
