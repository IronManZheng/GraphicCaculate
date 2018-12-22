import people_class

people_repository = []       #定义一个存储people信息的容器
edge_length_no_width = 0     #将无权重的路径长度设为全局变量
edge_length_width = 0        #将有权重的路径长度设为全局变量


def add_node(name):             #添加节点
    people_repository.append(people_class.People(name,None,None))



def remove_node(name):          #删除节点
    i = 0
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == name):
            #定义一个临时变量shadow_name临时存放正在被检测的库中的人名
            shadow_name = people_repository[i].get_node_atr()
            del people_repository[i]
            print("成功删除库中的元素:" + shadow_name)
        else:
            i += 1
    print("没有找到要删除的元素")



def add_edge(start,width,end):#start为边的起点，edge_name为边的名字，width为边的权重，end为边的终点
    #该方法主要检验start和end是否存在
    #只有当起点和终点同时存在时才可以添加边
    i = 0
    j = 0
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == start):
            while j < len(people_repository):
                if(people_repository[j].get_node_atr == end):
                    __add_edge__(start, width, end)
                else:
                    j += 1
        else:
            i += 1

    print("开始节点或终止节点不存在")

def __add_edge__(start,width,end):
    #该方法正式进行赋值
    i = 0
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == start):
            people_repository[i].put_next(end)
            people_repository[i].put_edge(end,width)      #*边的名字就用end的名字命名
        else:
            i += 1

def remove_edge(start,end):        #删除边
    i = 0
    j = 0
    while i < len(people_repository):
        if (people_repository[i].get_node_atr() == start):
            this_end = people_repository[i].get_neighbor_edge()
            while j < len(this_end[j]):
                if(this_end[j] == end):
                #将下一跳和与下一跳相连的边同时删掉
                    people_repository[i].remove_neighbors_iter(i)
                    people_repository[i].remove_neighbors_edge(end)
                else:
                    j += 1
        else:
            i += 1

        if(i >= len(people_repository)):
            #如果没有找到该节点，就返回1，否则返回0
            return 1
        else:
            return 0



def size_node():               #获得点的数量
    return len(people_repository)



def size_age(i):               # 获得边的数量
    return len(people_repository[i].edge)



def connectivity(test_start,test_end):     #判断任意两点的连通性
    i = 0
    j = 0
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == test_start):
            while j < len(people_repository[i].next[j]):
                m = find_next(None,people_repository[i].next[j],0)
                if(m != None):            #如果m不为空，即找到了m，则返回1
                    return 1
                else:
                    j += 1
            if (j == len(people_repository[i].next[j])):
                return 0                      #如果没有找到终点end，则返回0
        else:
            i += 1
    if(i == len(people_repository)):
        return 2                             #如果没有找到起点start，则返回2



def find_next(m,end,i):       #通过递归寻找连接的终点
    if(m.next != null):
        while i < len(m.next):
            m = m.next[i]
            if(m.get_node_atr == end):
                return m
            else:
                i += 1
                find_next(m,end,i)




def distanc(start,end):                 #计算两个节点之间的距离，无权重
    i = 0
    edge_length_no_width = 0            #每次调用该函数时先将该变量初始化一次
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == test_start):
            while j < len(None,people_repository[i].next[j],0):
                m = find_next_edge_no_width(people_repository[i].next[j])
                if(m != None):
                    return edge_length_no_width
                else:
                    return 0           #没有找到终点
        else:
            i += 1

def find_next_edge_no_width(m,end,i):         #由distance函数调用的递归函数
    if (m.next != null):
        while i < len(m.next):
            m = m.next[i]
            if (m.get_node_atr == end):
                return m
            else:
                i += 1
                find_next_edge_no_width(m,end,i)





def distanc_width(start,end):                 #计算两个节点之间的距离，有权重
    i = 0
    edge_length_width = 0            #每次调用该函数时先将该变量初始化一次
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == test_start):
            while j < len(None,people_repository[i].next[j],0):
                m = find_next_edge_no_width(people_repository[i].next[j])
                if(m != None):
                    return edge_length_width
                else:
                    return 0           #没有找到终点
        else:
            i += 1

def find_next_edge_width(m,end,i):         #由distanc_width函数调用的递归函数
    if (m.next != null):
        while i < len(m.next):
            m = m.next[i]
            if (m.get_node_atr == end):
                return m
            else:
                i += 1
                edge_length_width += m.edge[m.edge.next[n].get_node_atr()]   #暂时命名为n
                find_next_edge_no_width(m,end,i)




def has_node(graphic,node_name):        #判断图是否包含某一个点
    i = 0
    while i < len(graphic):
        if(graphic[i].get_node_atr() == node_name):
            return 1                    #如果包含，则返回1
        else:
            i += 1

    if(i == len(graphic)):
        return 0                       #如果不包含，则返回0




def has_edge(graphic,edge_name):       #判断一个图是否包含一条边
    i = 0
    j = 0
    while i < len(graphic):
        while j < len(graphic[i].next[j]):
            if(graphic[i].next[j].get_node_atr() == edge_name):
                return 1               #包含则返回1
            else:
                j += 1

    if(i == len(graphic)):             #不包含则返回0
        return 0

