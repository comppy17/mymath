def mymax(x, y):
    if x > y:
        return x
    else:
        return y

def listmax(l):
    lmax = 0
    for i in l:
        if i > lmax:
            lmax = i
    return lmax


if __name__ == "__main__":
    mylist = [1, 2, 3]
    print(listmax(mylist))
