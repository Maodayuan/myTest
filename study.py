class Clang:
    def __init__(self,name):
        self.name = name
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def delname(self):
        self.name='xxx'
clang=Clang('python')
print(clang.getname())
clang.setname('dd')
print(clang.getname())
clang.delname()
print(clang.getname())
print('hello world')