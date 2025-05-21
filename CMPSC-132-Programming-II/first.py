def square(numlist):
    add = 100
    for num in numlist:
        if num > 5 and num < 500 or num % 4 == 0:
            add = num * num
    return add
        