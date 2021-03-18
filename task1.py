def task(array):
    counter = 0
    for ar in array:
        counter += 1
        if ar == 0 or ar == '0':
            return counter - 1


print(task('111011110000'))
