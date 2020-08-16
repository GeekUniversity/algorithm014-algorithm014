学习笔记

1.本周主要学习了数组，链表，跳表，栈，队列，双端队列，优先队列的数据结构

2.时间复杂度，空间复杂度的定义

3.算法的两个核心思想，**升维和空间换时间**

4.数组的优点：查询方便，添加，删除元素效率低；链表刚好相反。

5.跳表引入了索引的概念，将查询的时间复杂度从O(n)减少为O(log n)



Queue   Java:

该类实现了boolean add(E e); 该方法可以往队列里添加元素，添加成功返回true。

如果add()方法被添加的元素超过队列的容量，抛出IllegalStateException异常

如果被添加的元素不允许加入，抛出ClassCastExcpetion异常

如果被添加的元素为空或该队列不允许空元素，抛出NullPointerException异常

如果被添加的元素的特征不符，抛出IllegalArgumentException异常

boolean offer(E e); 

该方法可以往队列里添加元素，添加成功返回true，失败返回false。

E remove();

移除队列头元素, 和poll()都返回队列头元素

remove()方法如果队列为空，抛出NoSuchElementException异常

E poll(); 

移除队列头元素，队列为空则返回空

E element();

检索，但不移除队列头元素，返回头元素，peek()的返回包括空值

element()方法如果队列为空，抛出NoSuchElementException异常



Deque  java:

双端队列的接口里和队列差不多，分为抛出异常和返回特殊值的接口。

不同的是，分头和尾。

头：抛出异常： addFirst(e);removeFirst();getFirst()

​       返回值：offerFirst(e);pollFirst();peekFirst()

尾：抛出异常： addLast(e);removeLast();getLast()

​       返回值：offerLast(e);pollLast();peekLast()



Priority Queue java:

该队列指定优先级排序，默认队列头是最小的元素。优先队列未实现同步，多个线程不应同时访问一个实例，应该用PriorityBlockingQueue类。

通过重写比较器，可以改变原来队列的优先级规则。

