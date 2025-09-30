class Employee:
    def __init__(self,id=123,Name='Unknown',Designation='Unknown',Salary='Unknown'):
        self.__id = id
        self.Salary = Salary
        self.Designation = Designation
        self.Name =  Name
    
    def get_id(self):
        return self.__id
    
    def set_id(self, value):
        self.__id = value 
    
        
    def travel(self,destination):
        print(f"traveling to {destination}")
        
        
    
em = Employee()
print(em.get_id())
em.set_id("432")
print(em.get_id())