def mymax(x, y):
    if x > y:
        return x
    else:
        return y

i = 1
j = 2
#print("The maximum of", i, "and", j, "is",  mymax(i, j) )
#print("The maximum of %d and %d is %d" % (i, j, mymax(i, j)))
#print("The maximum of {} and {} is {}".format(i, j, mymax(i, j)))
#print(f"The maximum of {i} and {j} is {mymax(i, j)}")


def listmax(l):
    lmax = 0
    for i in l:
        if i > lmax:
            lmax = i
    return lmax


mylist = [1, 2, 3]

print(__name__)

if __name__ == "__main__":
    print(listmax(mylist))
