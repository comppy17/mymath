import mymath
import unittest.mock as mock

def test_mymax():
    assert mymath.mymax(3, 5) == 5

@mock.patch('mymath.open')
def test_filemax(mock_open):
#   with open('test.dat', 'w') as f:
#       f.write("1\n")
#       f.write("5\n")
#       f.write("3\n")

#   with open('test.dat') as f:
#       fm = mymath.filemax(f)

    mock_open.return_value = ["1", "5", "3"]
    fm = mymath.filemax('test.dat')

    assert fm == 5
