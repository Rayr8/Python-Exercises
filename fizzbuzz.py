def fizz_buzz(max):
    result = []
    for i in range(max):
        if(i != 0):
            if(i % 4 == 0 or i % 6 == 0):
                if(i % 4 == 0 and i % 6 == 0):
                    continue
                result.append(i)
    print(result)
