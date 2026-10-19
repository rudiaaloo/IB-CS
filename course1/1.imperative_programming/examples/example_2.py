mark= int(input("Enter your mark: "))
if (mark >= 90):
    grade = '10'
elif (mark >= 70):
    grade = '9'
else:
    grade = '8'
print(f'Your grade is {grade}')