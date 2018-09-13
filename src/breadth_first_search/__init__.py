from collections import deque


def breadth_first_search(graph, root_node, fn):
    if not graph:
        return False

    search_queue = deque(graph.get(root_node, []))
    checked = {}

    while search_queue:
        node = search_queue.popleft()
        if not checked.get(node):
            if fn(node):
                return True

            checked[node] = True
            children = graph.get(node)
            if children:
                search_queue.extend(children)
    return False
