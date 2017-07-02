
def permutations(array):
    if len(array) == 0:
        return [[]]
    elif len(array) == 1:
        return [array]
    # list = []
    # for i in permutations(array):
    #     list.append(i)
    #     return
    else:
        list = [] #empty list
        for i in range(len(array)):
            var1 = array[i]
            var2 = array[:i] + array[i + 1:]
            for p in permutations(var2):
                list.append([var1] + p)
        return list
 
print(permutations([1]))