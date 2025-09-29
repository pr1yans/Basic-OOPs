class Employee:
    def __init__(self,id=123,Name='Unknown',Designation='Unknown',Salary='Unknown'):
        self.id = id
        self.Salary = Salary
        self.Designation = Designation
        self.Name =  Name
    
    def travel(self,destination):
        print(f"traveling to {destination}")
        
        
    
em = Employee(Salary=50000)

print(em.Salary)
em.travel("roorkee")