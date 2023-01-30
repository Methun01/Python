#Function Over Riding

class xyz_party:

    def ruling(self):
        self.party   = "ABC"

    def  RulingParty(self):
        print("The Current ruling party :",
               self.party)

class abc_party(xyz_party):

     def ruling(self):
         self.party = "XYZ"



obj_xyz = xyz_party()
obj_xyz.ruling()
obj_xyz.RulingParty()

obj_abc = abc_party()
obj_abc.ruling()
obj_abc.RulingParty()


#




                
