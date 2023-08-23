class calculator():
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def add(self):
    print("Sum :",self.x+self.y)

  def subtraction(self):
    print("Subtraction :",self.x-self.y)  

  def multiplication(self):
    print("Multiplication :",self.x*self.y)

  def division(self):
    print("Division :",self.x/self.y)  
#x=int(input("Enter first number : "))
#y=int(input("Enter second number : "))
#n1=calculator(x,y) # object 
n1=calculator(5,4) # object 

n1.add()
n1.subtraction()
n1.multiplication()
n1.division()