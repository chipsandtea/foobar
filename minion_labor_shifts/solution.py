def answer(data, n):
    # data - arr 
    # any num in data can't occur more than n times
    # O(n) to scroll & count num of occurrences 
    
    counted = dict()
    print(data)
    print("n: " + str(n))
    for num in data:
        if num in counted:
            counted[num] += 1
        else:
            counted[num] = 1
    print(counted)
    valid = []
    for key, value in counted.items():
        if value > n:
            for i in range(value):
                data.remove(key)
    return data