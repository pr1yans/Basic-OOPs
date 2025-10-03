class Animal:
    def __init__(self, Name):
        self.Name = Name
        
    def speak(self):
        print(f"animal makes sound {self.Name}")
        
        
class Dog(Animal):
    def __init__(self, Name):
        super().__init__(Name)
    def speak(self):
        super().speak()
        print(f"{self.Name} barks")
        
        
a  = Animal('billy')
a.speak()

d = Dog("tommy")
d.speak()