# 题目要求
通过合作电影，找到两人之间的最短路径

# 数据结构
## people
people是一个字典，字典的key是演员的id,value是一个字典，字典的内容包含名字和电影，其中电影是一个set，包含电影的id

## names
names是一个字典，字典的key是人名，value是一个set，内容为演员的id

## movies
movies是一个字典，字典的key是电影的id,value是一个字典，字典的内容包含电影的名字和演员，其中演员是一个set,包含演员的id

# 如何找到邻居
source和target都是演员的id，所以是要找演员的id的邻居

演员id->电影的id->演员id

# 广度还是深度
在没有“最多6个人”的先验条件下，使用广度可以找到最短的路径