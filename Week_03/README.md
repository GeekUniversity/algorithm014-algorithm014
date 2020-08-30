学习笔记

递归python代码模板

def reursion(level,params1,params2,...):

​		if level > MAX_LEVEL:

​				process_result

​                return

​		process(level,data)

​        self.recursion(level+1, p1,...)

思维要点：

1.不要人肉递归

2.找到最近最简方法，将其拆解成可重复解决的问题

3.数学归纳法思维

分治代码模板

def divide_conquer(problem,.param1,param2,...):

​		if problem is None:

​				print_result

​				return

​		data = prepare_data(problem)

​        subproblems = split_problem(problem,data)

​		subresult1 = self.divide_conquer(subproblems[0],p1,...)

​		subresult2 = self.divide_conquer(subproblems[1],p1,...)

​		subresult3 = self.divide_conquer(subproblems[2],p1,...)

​		result = process_result(subresult1,subresult2,subresult3,...)