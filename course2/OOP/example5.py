completed = False 
while not completed:
    try: 
        filename = input('Enter file name: ')
        with open(filename, 'at') as f: #flag of a means whatever writing we do it goes to beginning of file
            print(440, file=f)
        completed = True #if an exception is raised this value is never evaluated and the loop continues
    except Exception as e:
        print('nope try again', e)