class Animal():
    name='Amy'
    sound='grunt'
    size='large'
    color='hair'
    def getColor(self):
        return self.color
    #setting makeNoise as a property and now we will be able to invoke it without ()
    @property 
    def makeNoise(self):
        return self.sound
    def setColor(self,color):
        self.color=color
    def setNoise(self,sound):
        self.sound=sound



#Dog class inherits from Animal..in python we just pass the class name as an arg
class Dog(Animal):    
    name='Tommy'

myPet=Dog()
print(myPet.getColor())
print(myPet.makeNoise) #calling makeNoise without any () since its a property now rather than a method
myPet.color='white'
print(myPet.getColor())

myPet.setColor('blue')
myPet.setNoise('barks')
print(myPet.getColor())
print(myPet.makeNoise)


email="rjtbansal@gmail.com"
to_list=['jsmith@gmail.com','jwhite@yahoo.com']
from_list=['someone@example.com','someperson@gmail.com']

def sendEmail(email,to=to_list, from_list=from_list):
    pass #use pass when function is empty else python complains

#to and from_list are keyword arguments and they are optional, email is positional arguments
#in python postional arguments always appear first and then we can specify keyword args
sendEmail(email, to=['jsmith@gmail.com'], from_list=['someone@example.com'])
