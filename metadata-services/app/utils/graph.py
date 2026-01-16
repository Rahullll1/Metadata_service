def has_path(graph: dict, start: int, target: int, visited=None) -> bool:
    """
    DFS to check if there is a path from start to target.
    """
    if visited is None:
        visited = set()

    if start == target:
        return True

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if has_path(graph, neighbor, target, visited):
                return True

    return False
