#Diamond shaped inheritence

#SuperClass
class HOD:
    def tot_sdnts(self):
      print("This depatment has total strength of 103 students")
    

class I_bsc(HOD):
    def I_sdnts(self):
      self.strength = 33
      print("1st Year has the strength  of ",
            self.strength)


class II_bsc(HOD):
    def II_sdnts(self):
      self.strength = 34
      print("2nd Year has the strength  of ",
            self.strength)

class III_bsc(I_bsc, II_bsc):
    def III_sdnts(self):
      self.strength = 36
      print("3rd Year has the strength  of ",
            self.strength)

obj_attendness = III_bsc()
obj_attendness.I_sdnts()
obj_attendness.II_sdnts()
obj_attendness.III_sdnts()
obj_attendness.tot_sdnts()

    
