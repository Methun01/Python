#Single Inheritence

#Base Class
class RollsRoyce:  

    company = "RollsRoyce"
    founder = "Charles & Henry"
    comp_type = "Automobile [Cars]"
    car_type  = "Luxury Cars"
    headquarters = "Derby, UK"

#derive class
class RR_phantom(RollsRoyce):  
    def __init__(self):
        self.model = "RR Phantom VIII"
        self.price = "Approx. Rs.9,50,00,000"
        
    def enquiry(self):
        print("Car Model   :", self.model)
        print("Market Price:", self.price)

    def comp_detail(self):
        print("Company     :", self.company)
        print("Company Type:", self.comp_type)
        print("Founders    :", self.founder)


#object declaration
obj_phantom = RR_phantom()      

print("Available Models :\n  1. PHANTOM VIII\n  2. Company Details")
model = int(input("Enter the Model Number to view details :"))

if model==1 :
    obj_phantom.enquiry()
elif model==2 :
    obj_phantom.comp_detail()
else:
    print("Enter Valid Model Number")


#Multiple Inheritence

#super class1
class south_IN:
    def south_pop(self):
        print("South India has less population compared to North")

#super class2
class north_IN:
    def north_pop(self):
        print("North India has more population compared to South")

#MultiDerived  class
#access both super classes in this class        
class IN(south_IN, north_IN):
    pass

obj_IN = IN()

#Accessing from super class 1 & 2 from MultiDerived Class
obj_IN.north_pop()
obj_IN.south_pop()


#Multilevel Inheritence

#super class
class national_lvl:
    def national_players(self):
        print("players selected from state level")

#derived class1
class state_lvl(national_lvl):
    def state_players(self):
        print("players selected form district level")

#derived class2
class district_lvl(state_lvl):
    def district_players(self):
        print("players from academy and Eductional Institutions")


obj_district = district_lvl()        

#access super class method
obj_district.national_players()

#access derived class1 method
obj_district.state_players()

#access same class method
obj_district.district_players()
    
