from collections import deque
import heapq
from task_4 import build_heap_tree, draw_tree

def generate_colors(n, start_color="#063D91", end_color="#6BB3E4"):
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0,2,4 ))
    
    def rgb_to_hex(rgb_color):
        return "#{:02X}{:02X}{:02X}".format(*rgb_color)
    
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    colors=[]
    for i in range(n):
        ratio = i / max(n-1, 1)
        interp = tuple(int(start_rgb[j] + (end_rgb[j] - start_rgb[j])*ratio) for j in range(3))
        colors.append(rgb_to_hex(interp))

    return colors 

def dfs_visualize(root):
    if not root:
        return
    
    stack = [root]
    visited = []
    nodes =[]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            nodes.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    colors = generate_colors(len(nodes))
    for node, color in zip(nodes, colors):
        node.color = color


if __name__=="__main__":
    data = [4, 10, 3, 5, 1]
    heapq.heapify(data)
    root = build_heap_tree(data)

    dfs_visualize(root)
    draw_tree(root)
