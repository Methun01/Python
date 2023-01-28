#Abstraction and Encapsulation


class my_purse:

    def __init__(self,currencies):
        self.currencies = currencies

    def display_purse(self):
        print("My purse has currencies of : ")
        for note in self.currencies:
            print(note)

    def borrow_currency(self,borrow_currency):

        if borrow_currency in self.currencies:
            print("Get Money And Try to Return Soon as possible")
            self.currencies.remove(borrow_currency)
        else:
            print("Hmm I don't have that currency")

    def receive_currency(self, receive_currency):
        print("You Already returned My Money back :)")
        self.currencies.append(receive_currency)


currencies = ['10', '20', '50', '100', '500',]
obj =  my_purse(currencies)

availability = "1.Check Availability\n2.Borrow Money\n3.Return Money"

while True:
    print(availability)
    mthd = int(input("Enter Your Choice of Method in Number : "))

    if mthd == 1:
        obj.display_purse()
    elif mthd == 2:
        currency = input("Enter Currency to borrow")
        obj.borrow_currency(currency)
    elif mthd == 3:
        currency = input("Enter Currency to Return")
        obj.receive_currency(currencies)
    else:
        print("Select Available Options Only.")
        quit()

    
      
        
