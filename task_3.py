import heapq
import networkx as nx

weighted_roads =[
    ('A', 'B', 4), ('A', 'C',2), ('B', 'D',5), ('C','D', 1), ('D', 'E',3), ('E', 'F',1), ('C', 'F',7)
]

G=nx.Graph()
for u,v, weight in weighted_roads:
    G.add_edge(u,v, weight= weight)

def dijkstra_all(graph, start_node):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node]=0

    priority_queue=[(0, start_node)]

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor]['weight']
            total_cost = current_cost + edge_weight

            if total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return distances


if __name__=="__main__":
    start ="A"
    shorted_distances = dijkstra_all(G, start)

    for node, dist in shorted_distances.items():
        print(f"{start} -> {node} = {dist}")
