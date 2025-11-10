n = input('enter the number ')
n = int(n)
result = [0,1]
for i in range(n-2):
    last_element = result[-1]
    lastsecond_element = result[-2]
    next_fib = last_element + lastsecond_element
    result.append(next_fib)
print(result)
