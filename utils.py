
def if_same(a,b):
    for i in range(len(a)):
        if a[i] in b and i == len(a)-1:
            return 1

    return 0

def getSubsets(a):
    result = [[]]
    size = len(a)
    for i in range(size):
        for j in range(len(result)):
            result.append(result[j] + [a[i]])
    result.remove(result[0])
    result.remove(result[-1])
    return result

def get_count(a,data):
    count =0
    for item in data:
        for i in range(len(a)):
            if a[i] in item and i==len(a)-1:
                count = count+1
    return count



