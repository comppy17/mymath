import mymath

def test_mymax():
    assert mymath.mymax(3, 5) == 5

def test_filemax():
#   with open('test.dat', 'w') as f:
#       f.write("1\n")
#       f.write("5\n")
#       f.write("3\n")

#   with open('test.dat') as f:
#       fm = mymath.filemax(f)

    fake_file = ["1", "5", "3"]
    fm = mymath.filemax(fake_file)

    assert fm == 5
