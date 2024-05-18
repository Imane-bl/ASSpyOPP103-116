class User:
  # Write Class Content
  def __init__(self,name,sec,age,gender):
    self.name=name
    self.sec=sec
    self.age=age
    self.gender=gender
    self.deffre=40-age

    if self.gender=='Male':
     self.res="Mr"
    elif self.gender=='Female':
     self.res="Mrs"
    else:
      return " "
    
  
    if self.deffre<10:
       self.res1="0"
    else:
       self.res1=""
  
  def full_details(self):
    
      
       return f"Hello {self.res} {self.name} {self.sec[0]}. [{self.res1}{self.deffre}] Years To Reach 40"
      

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40