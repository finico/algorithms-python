from collections import deque


def breadth_first_search(graph, root_node, fn):
    if not graph:
        return False

    search_queue = deque()
    search_queue += graph[root_node]
    checked = {}

    while search_queue:
        node = search_queue.popleft()
        if not checked.get(node):
            if fn(node):
                return True
            else:
                search_queue += graph[node]
                checked[node] = True
    return False
