class People():   #定义人员的类
    def __init__(self,name,next,edge):
            self.name = name
            self.next = []
            self.edge = ()


    def put_next(self,people_class):      #给下一跳next赋值
        self.next.append(people_class)


    def put_edge(self,edge_name,width):      #给两跳之间的连线也就是边赋值
        self.edge[edge_name] = width         #边的名字被命名为字典的键，边的权重被命名为字典的值
        return

    def get_node_atr(self):  #获得节点的名称
        return(self.name)

    def get_neighbors_iter(self): #获得节点的所有下一跳
        return(self.next)

    def get_neighbor_edge(self):  #获得节点的所有相邻边
        return(self.edge)

    def remove_neighbors_iter(self,i):   #删除节点的下一跳
        del self.next[i]

    def remove_neighbors_edge(self,end):
        del self.edge[end]