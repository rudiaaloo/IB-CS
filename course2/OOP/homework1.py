class Book: 
    def __init__(self, title, authors, publication_year):
        self.title = title 
        self.authors = authors #how does it know this would be int/array/ list
        self.publication_year = publication_year

#string representation
    def __str__(self):
        auth = "&".join(self.authors)
        return f"{auth}: {self.title} ({self.publication_year})" #why do we still need to use the self if we have defined it as a varibale? 

    def __num_authors(self):
        return len(self.authors)

clrs = Book("introduction to alorithms", ["cormen", "leiserson", "rivest", "stein"], 2009)

print(clrs)