import people_class

people_repository = set()       #定义一个存储people信息的set容器


def add_node(name):             #添加节点
    people_repository.add(people_class.People(name,None,None))




add_node("KK")
print(people_repository)
