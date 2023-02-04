#code for Depth First Search

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self, x, y):
        self.graph[x].append(y)
        
    def DFSUtil(self, y, explored, goal, path):
        explored[y - 1] = True
        path.append(y)
        if y == goal:
            return True
        for i in self.graph[y]:
            if not explored[i - 1]:
                if self.DFSUtil(i, explored, goal, path):
                    return True
        path.pop()
        return False

    
    def DFS(self, start_state, goal_state):
        explored = [False for i in range(1, self.V + 1)]
        path = []
        if self.DFSUtil(start_state, explored, goal_state, path):
            return path
        return None
    
def main():
    with open("i1.txt") as f:
        total_states = int(f.readline().strip())
        g = Graph(total_states)
        for i in range(1, total_states + 1):
            line = f.readline().strip().split()
            for j in line:
                g.addEdge(i, int(j))
        start_state = int(f.readline().strip())
        goal_state = int(f.readline().strip())
        path = g.DFS(start_state, goal_state)
        if path:
            print("Traversed States: ")
            print(path[0],end="")
            for i in range(1,len(path)):
                print("-->", end="")
                print(path[i], end=" ")
            print("\n")
            print("Path:", path)
        else:
            print("Path does not exist")

if __name__ == "__main__":
    main()
