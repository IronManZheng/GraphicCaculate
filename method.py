import people_class

people_repository = []       #定义一个存储people信息的容器


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



def add_edge(start,edge_name,width,end):#start为边的起点，edge_name为边的名字，width为边的权重，end为边的终点
    #该方法主要检验start和end是否存在
    #只有当起点和终点同时存在时才可以添加边
    i = 0
    j = 0
    while i < len(people_repository):
        if(people_repository[i].get_node_atr() == start):
            while j < len(people_repository):
                if(people_repository[j].get_node_atr == end):
                    __add_edge__(start, edge_name, width, end)
                else:
                    j += 1
        else:
            i += 1

    print("开始节点或终止节点不存在")

def __add_edge__(start,edge_name,width,end):
    #该方法正式进行赋值
    return