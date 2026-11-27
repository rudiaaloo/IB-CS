class Newspaper:
    def __init__(self, name=str, year=int, month=int, day_of_month=int, is_finnish=bool ):
        self.__name = name
        self.year = year 
        self.month = month 
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish 

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"({self.__name}, {self.year}, {self.month}, {self.day_of_month}, {self.is_finnish})"

crlt = Newspaper("Newyorktimes", [1989], [12], [25], False)

print(crlt)