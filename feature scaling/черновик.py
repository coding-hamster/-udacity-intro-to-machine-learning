""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    maximum = 0
    minimum = 10e10
    for i in arr:
        if i > maximum:
            maximum = i
        else:
            pass
    for i in arr:
        if i < minimum:
            minimum = i
        else:
            pass
    b = maximum - minimum
    list = []
    for i in arr:
        a = i - minimum
        c = a/b
        print(i, c)
        list.append(c)
    return list

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print (featureScaling(data))

