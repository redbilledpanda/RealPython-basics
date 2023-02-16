# this little code snippet demonstrate
import datetime
import pdb

class truck:

    species = "Motor vehicles"

    def __init__(self, make, model, registration):
        self.make = make
        self.model = model
        self.registration = registration

    def __repr__(self):
        return f"Car registered as \"{self.registration}\" is a {self.make} {self.model}"

    def SetSellingPrice(self):
        self.SellingPrice = int(input("What is your selling price?: "))

    def SetMileage(self):
        self.Mileage = int(input("How much miles do you have on it?: "))

    def SetRegistrationYear(self):
        self.RegistrationYr = int(input("What is it's registration year?: "))

    def GetBasicDetails(self):
        return (self.make, self.model, self.registration)

    def GetMileage(self):
        return self.Mileage

    def GetSellingprice(self):
        return self.SellingPrice

    def GetRegistrationYear(self):
        return self.RegistrationYr

Truck1 = truck("Ford", "F-150", "California 921553")

print(Truck1)

Truck1.SetSellingPrice()
Truck1.SetMileage()
Truck1.SetRegistrationYear()

# this is one way to break long f-strings in which we DO NOT want to format the output
# also shown here how to INCLUDE newlines in a f-string as directly appending a string
# with \n throws an error
newline = '\n'
print(f"User asks ${Truck1.SellingPrice} for his {Truck1.make} {Truck1.model} with " \
        f"{Truck1.registration.split()[0]} plates{newline}"
        f"It has {Truck1.Mileage} miles on it and was registered in {Truck1.RegistrationYr}");

def CheckFairPrice(vehicle):
    #pdb.set_trace()
    (make, model, plates) = vehicle.GetBasicDetails()

    if ((make != "Toyota") or (make != "Honda")):
        # how many days since the vehicle was on the road (approx)?    
        numdays = (datetime.date.today().year - int(vehicle.GetRegistrationYear())) * 360

        # Has the fella driven more than a 100 miles everyday?
        hundredRun = True if ( vehicle.GetMileage()/numdays >= 100) else False

        # if this vehicle ran for an avg 100 miles a day and if it's more than
        # 5 yrs old, it shouldn't sell for more than 5000 period
        if (hundredRun):
            if ((datetime.date.today().year - int(vehicle.GetRegistrationYear())) - 5):
                if (int(vehicle.GetSellingPrice) > 5000):
                    print("price is not fair")
                else:
                    print("price is fair")
        else:
            print("price fairness not evaluated for now")
        
CheckFairPrice(Truck1)
