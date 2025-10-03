#  multilevel

"""class Parent:
    def __init__(self,name):
        self.name = name
        
    def rm(self):
        print(f"we are working {self.name}")
        
class Child(Parent):
    def work(self):
        print(f"we are playing {self.name}")
        
class little(Child):
    def work(self):
        print(f'we are sleeping {self.name}')
        
        
        


c = little('rony')
c.rm()"""

#hierarichal

"""class Parent:
    def __init__(self,name):
        self.name = name
        
    def rm(self):
        print(f"we are working {self.name}")
        
class Child(Parent):
    def work(self):
        print(f"we are playing {self.name}")
        
class little(Parent):
    def hui(self):
        print(f'we are sleeping {self.name}')
        
        
        


c = little('rony')
c.rm()"""
#diamond 

class Parent:
    def __init__(self,name):
        self.name = name
        
    def rm(self):
        print(f"we are working {self.name}")
        
class Child(Parent):
    def wo(self):
        print(f"we are playing {self.name}")
        
class Little(Parent):
    def work(self):
        print(f'we are sleeping {self.name}')
        
class Mom(Little,Child):
    def job(self):
        print(f"takes care of {self.name}")




m = Mom("ruby")
m.rm()    
        
        
        


