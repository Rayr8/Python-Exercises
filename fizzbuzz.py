def fizz_buzz(max):
    result = []
    for i in range(1, max):
        if(i % 4 == 0 or i % 6 == 0)and not (i % 4 == 0 and i % 6 == 0):
          result.append(i)
    return result

print(fizz_buzz(20))
