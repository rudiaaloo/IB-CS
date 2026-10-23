try: 
    import pathlib
    file_path = pathlib.Path('data')/'points.txt'
    with open(file_path) as f:
        points_read = []
        for line in f:
            [x, y] = [int(word) for (word) in line.split()]
            points_read.append(Point(x, y))
        print(points_read[-1])
    except Exception as e:
        print('exception:', e)