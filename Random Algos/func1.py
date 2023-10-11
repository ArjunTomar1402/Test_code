import sys
f_counter = 0

def func1():
    global f_counter
    print(sys.getsizeof(sys._getframe()))
    f_counter +=1
    a = 2
    b = 3
    c = 4 
    print("in 1")
    func2()
def all():
    sf=sys._getframe()
    print(sf)

def func2():
    global f_counter
    print(sys.getsizeof(sys._getframe()))
    f_counter +=1
    print("in 2")
    if f_counter==6:
        sys.exit(0)
    func1()

func1()
# print(sf)