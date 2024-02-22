class Person:
    def __init__(self, name,lastname):
        self.name = name
        self.lastname = lastname
        
    def display_info(self):
        print(f"Navn:{self.name},Efternav:{self.lastname}")    