学习笔记

贪心算法

贪心算法是一种在每一步选择中都采取在当前状态下最好或最优的选择，从而希望导致结果是全局最好或最优的算法。

贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保持以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

DFS代码 递归写法

visited = set()	

def dfs(node, visited):

​		visited.add(node)

​        ...

​       for next_node in node.children():

​              if not next_node in visited:

​                     dfs(next node, visited)

BFS代码

def BFS(graph, start, end):

​		visited = set()

​		queue = []

​        queue.append([start])

​        while queue:

​                   node = queue.pop()

​                   visited.add(node)

​                   process(node)

​                   node = generate_related_nodes(node)

​                   queue.push(nodes)