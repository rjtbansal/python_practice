class Animal():
    name='Amy'
    sound='grunt'
    size='large'
    color='hair'
    def getColor(self):
        return self.color
    def makeNoise(self):
        return self.sound

#Dog class inherits from Animal..in python we just pass the class name as an arg
class Dog(Animal):    
    name='Tommy'

myPet=Dog()
print(myPet.getColor())
print(myPet.makeNoise())
myPet.color='white'
print(myPet.getColor())
