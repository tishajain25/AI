#code for Breadth First Search

def BFS(graph, initial, goal):
    queue = []
    visited = set()
    parent = {}
    queue.append(initial)
    visited.add(initial)
    
    while queue:
        state = queue.pop(0)
        if state == goal:
            path = [goal]
            while path[-1] != initial:
                path.append(parent[path[-1]])
            path.reverse()
            return path, visited
        
        for neighbour in graph[state]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = state
    return None, visited

with open("i1.txt") as f:
    num_states = int(f.readline())
    graph = {}
    
    for i in range(1, num_states + 1):
        neighbours = list(map(int, f.readline().split()))
        graph[i] = neighbours
    initial = int(f.readline())
    goal = int(f.readline())

path, visited = BFS(graph, initial, goal)

if path:
    print("Traversed States:", visited)
    print("Path from Initial State to Goal State:", path)
else:
    if goal not in graph.keys():
        print("Goal state not present in the state space.")
    else:
        print("Goal state not approachable from the initial state.")
