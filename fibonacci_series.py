if n == 3:
    last_element = in_list[-1]
    secondfrom_last = in_list[-2]
    next_fib = last_element + secondfrom_last
    result.append(last_element + secondfrom_last)
elif n == 4:
    last_element = in_list[-1]
    secondfrom_last = in_list[-2]
    next_fib = last_element + secondfrom_last
    result.append(last_element + secondfrom_last)
    s_result = result[-1] + result[-2] 
    result.append(s_result)