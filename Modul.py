data = [int(i) for i in input().split()]
def more_than_five(data):
    data1= []
    for element in data:
        if abs(element)>=5:
            data1.append(element)
    return data1
print(more_than_five(data))


