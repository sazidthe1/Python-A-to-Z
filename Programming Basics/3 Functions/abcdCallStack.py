def a():
    print('a() starts')
    b()
    d()

def b():
    print('b() starts')
    c()
    print('b() starts')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()