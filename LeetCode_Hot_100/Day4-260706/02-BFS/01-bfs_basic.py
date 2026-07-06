
import queue


def bfs_basic(graph, start_node):
    """
    BFS algorithm basic flow:
    1. Initialize queue q = queue()
    2. Enqueue start node q.push(s)
    3. Mark visited vis[s] = true
    4. Loop until queue empty:
       - Dequeue u = q.pop()
       - Iterate unvisited neighbors v ∈ neighbor(u) ∧ vis[v] == false
       - Mark visited vis[v] = true
       - Enqueue q.push(v)
    """
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    visited.add(start_node)

    while not q.empty():
        u = q.get()
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
