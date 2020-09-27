学习笔记

剪枝

双向搜索：双向BFS

启发式搜索

估价函数

启发式函数： h(n), 它用来评价哪些结点最有希望的是一个我们要找的结点， h(n)会返回一个非负实数， 也可以认为是从结点n的目标结点路径的估计成本。

启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。

A*代码模板

def AstarSearch(graph, start, end):

​	pq = collections.priority_queue() # 优先级 —> 估价函数

​	pq.append([start]) 

​	visited.add(start)

​	while pq: 

​		node = pq.pop() # can we add more intelligence here ?

​		visited.add(node)

​		process(node) 

​		nodes = generate_related_nodes(node) 

  unvisited = [node for node in nodes if node not in visited]

​		pq.push(unvisited)

AVL树：

Balance Factor(平衡因子)：

是它的左子树的高度减去它的右子树的高度（有时相反）。

balance factor = {-1, 0 ,1}

通过旋转操作来进行平衡（四种：左旋，右旋，左右旋，右左旋）

不足：结点需要存储额外信息，且调整次数频繁

红黑树：

近似平衡的二叉搜索树， 能够确保任何一个结点的左右子树的高度差小于两倍

特点：

每个结点要么是红色，要么是黑色

根节点是黑色

每个叶节点是黑色的

不能有相邻接的两个红色结点

从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点

读操作很多，但写操作很少的情况下，用AVL树

如果查询，插入操作比较多，用红黑树

