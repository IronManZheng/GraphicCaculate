class People():
    def __init__(self,name,age,next):
        self.name = name
        self.age = age
        self.next = next
    def run_all(self):
        return(self.name,self.age,self.next)


myReposity = set()
PiPi = People('HAHA',28,None)
DaDa = People('Kevin',26,PiPi)
myReposity.add(DaDa)
myReposity.add(PiPi)
print(DaDa.next.run_all())
