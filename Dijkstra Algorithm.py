edges, V = map(int, input().split())
start, end = map(int, input().split())

graph = {i: [] for i in range(1, V + 1)}
costs = {i: float('inf') for i in range(1, V + 1)}
parents = {i: -1 for i in range(1, V + 1)}
processed = []

# ввод рёбер
for _ in range(edges):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))   # сохраняем вес

costs[start] = 0  # стартовая вершина

def find_lowest_cost_node():
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs:
        if node not in processed and costs[node] < lowest_cost:
            lowest_cost = costs[node]
            lowest_node = node
    return lowest_node


def Dijkstra(end):
    node = find_lowest_cost_node()
    while node is not None:
        for neighbor, weight in graph[node]:
            new_cost = costs[node] + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_cost_node()
    return costs[end]


print(f"Расстояние от вершины {start} до вершины {end}: {Dijkstra(end)}")