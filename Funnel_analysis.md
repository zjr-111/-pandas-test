                                          集合操作
想要进行集合的操作
要先将列表转换为集合  通过set() 函数
  操作              简写             结果
len()                          s集合中的元素个数
x in s                         判断x是否是集合s中的元素
x not in s                     判断x是否不是集合s中的元素
s.issubset(t)      s <= t      判断集合s是否是t的子集，即s的所有元素也都是t的元素
s.issuperset(t)    s >= t      判断集合s是否是t的超集，即t的所有元素也都是s的元素
s.union(t)         s | t       s和t的并集，即构造一个新集合，使其元素为s和t的元素的总和
s.intersection(t)  s & t       s和t的交集，即构造一个新集合，其元素即在s中也在t中
s.difference(t)    s - t       t相对于s的补集，即构造一个新集合，其元素在s中但不在t中
