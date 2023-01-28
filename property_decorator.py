#Using Property Decorator
class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property    
    def msg(self):  
        return "Your Name is " + self.name + " and " + str(self.age) + "years age"
        

o = info("methun", "19")
print(o.name)
print(o.age)
print(o.msg)  #gives age = 19.
o.age = 20   
print(o.msg)  #gives age = 20.



#Getter and Setter

class mark:

    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, t):
        if t < 0 or t > 500:
            print("Hmm., Looks like you miss Spelled.. Try again.")
        else:
            self._total = t
    


total = mark(float(input("Enter Your Total Marks :" )))
print("Your Average is :",total.average())



total = mark(float(input("Enter Your Total Marks :" )))
print("Your Average is :",total.average())






#Getter & Setter using a Function:

class mark:

    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5.0

    def getter(self):             
        return self._total

    def setter(self, t):
        if t < 0 or t > 500:
            print("Hmm., Looks like you miss Spelled.. Try again.")
        else:
            self._total = t

    total = property(getter, setter)       
    


total = mark(float(input("Enter Your Total Marks :" )))
print("Your Average is :",total.average())



total = mark(float(input("Enter Your Total Marks :" )))
print("Your Average is :",total.average())




#Class Method Decorator

class fruits:

    count = 0                                #variable for iteration

    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
        fruits.count += 1                    #iterate every time when __init__() called.

    def printDetail(self):              
        print("Name :", self.name, "\nQuality :", self.quality)

    @classmethod
    def stock(cls):
        return cls.count


x = fruits(input("Enter Fruit Name : "), input("Enter the Quality fresh or rotten : "))
x.printDetail()                                   #prints values stored in x
print("Total Stocks Available : ",fruits.stock()) #prints total no.of.times __init__() used 

y = fruits(input("Enter Fruit Name : "), input("Enter the Quality fresh or rotten : "))
y.printDetail()                                   #prints values stored in y
print("Total Stocks Available : ",fruits.stock()) #prints total no.of.times __init__() used 






