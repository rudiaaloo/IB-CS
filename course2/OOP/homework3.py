class Course:
    def __init__(self, name, topic, name_teachers, nofpart): #kinda like class verison of python paramters, makes sure it applies to all objects 
        self.name = name 
        self.topic = topic 
        self.name_teachers = name_teachers 
        self.nofpart = nofpart 
    def __str__(self):
        return f"({self.name}, {self.topic}, {self.name_teachers}, {self.nofpart})"

    