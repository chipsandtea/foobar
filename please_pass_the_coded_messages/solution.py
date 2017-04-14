def answer(l):
    # The idea is that the sum of all digits must be divisible by 3
    # All multiples of 3 meet that so, lets start there
    print(l)
    valid = [i for i in l if i % 3 == 0]
    print('valids: ' + str(valid))

    # remove then from l (there should be a better way)
    test = [i for i in l if i % 3 != 0]
    test.sort(reverse=True)
    print('test: ' + str(test))

    temp = []
    for beginning in range(len(test)):
        end = len(l)
        #increment first letter, then scroll to the end of the list.
        # essentially all permutations and storing the largest subset all times
        while end >= beginning:
            #construct window
            wind = test[0:beginning] + test[end:len(test)]
            #print(wind)
            curr_sum = sum(wind)
            if curr_sum % 3 == 0:
                print('window: ' + str(wind) + ' sum: ' + str(curr_sum))
                if len(wind) > len(temp) or (len(wind) == len(temp) and curr_sum > sum(temp)):
                    temp = wind
            end -= 1
    valid = valid + temp
    valid.sort(reverse = True)
    valid = int(''.join(str(digit) for digit in valid) or 0)
    return valid
print(answer([3,1,4,1,5,9]))