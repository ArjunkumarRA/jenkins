import  pytest

@pytest.fixture()
def fac(n):
    if n<0:
        print("Enter a Postive Number")
    elif (n==1 or n==0):
        return 1
    else:
        return n * fac(n-1)
    print("The factorial of the entered number : ", fac(n))
n=5


def test_num():
    assert type(n) == int
def test_size():
    assert n==5
