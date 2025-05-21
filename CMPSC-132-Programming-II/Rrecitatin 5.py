

def hailstone(num):
    
    if num == 1: #when num = 1 stop the loop
        return [num]
    elif num % 2 == 0: # if number even divide by 2
        return [num] + hailstone(num / 2)
    
    else: # if number odd multiply by 3 then add 1
        return [num] +  hailstone(3 * num + 1)

