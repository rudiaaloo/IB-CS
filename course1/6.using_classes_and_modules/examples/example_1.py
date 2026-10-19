str.replace
print(help(str.replace))
#return all occurrences replaced by new string
txt = "What is this?" 
print(txt.replace(' ', 'pause', count = 1)) #replace only first occurrence with count parameter
#you use these in larger projects 
#when self is the first parameter, you can ignore it when using the object, but not the class
#example:
print(str.replace(txt, ' ', 'pause', count = 1))