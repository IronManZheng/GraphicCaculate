class People():   #定义人员的类
    def __init__(self,name,next,edge):
        if(next != None or edge != None):
            self.name = name
            self.next = set()     #相邻的节点用set数据类型进行存储
            self.edge = ()        #相邻的连接边用字典类型进行存储
        else:
            self.name = name
            self.next = None
            self.edge = None

    def get_node_atr(self):  #获得点的属性
        return(self.name)

    def get_neighbors_iter(self): #获得相邻点和相邻边的属性
        return(self.next,self.edge)