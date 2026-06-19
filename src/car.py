class car: 
    def __init__(self, model, year, color, for_sale): #here self is the class itself and we __init__ is a dunder method we are making a constructor here
        self.model = model
        self.year = year        #instance of  class
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.model}")

    def stop(self):
        print(f"you stopped the {self.model}")
