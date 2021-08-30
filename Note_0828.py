# The following is the note about Introduction to Computation and Programming Using Python、
# and the note about MIT Introduction to computational thinking and data science

# Objects have types. Types are either scalar or non-scalar.
# Scalar: int, float, bool, None. indivisible.

# condition
x = 3
y = 9
z = 7
print((x if x>z else z) if x > y else (y if y>z else z))

# f string, {} means the thing inside is replaced
num = 100
fraction =  1/2
print(f'{int(num*fraction)} is {fraction*100}% of {num}')

# 2.4.1 Input
'''

name = input('Enter your name: ')
# return what you enter as name
print('Are you really', name, '?')
# Use f string to avoid space between name and ?
print(f'Are you really {name}?')

'''

# class and object
# create class

class classmate():
    def study(self):
        print('the student is studying')
        # self is  the obejct that uses the method
        print(self)

haozhi = classmate()
liubo = classmate()

print(haozhi)
print(liubo)

haozhi.study()
liubo.study()

# add character to the object outside
haozhi.hight = 180

# get the attribute which is outside of object
# use the name of object to get the attribute
print(f'hight of haozhi is {haozhi.hight}')

# use self to get the attribute
class teacher():
    def print_info(self):
        print(f'the age of the teacher is {self.age}')
yuhao = teacher()
teacher.age = 44
yuhao.print_info()

# magic method _init_()
# create attribute when create the class

# magic method is used by default when create a new instance

class girlfriend():
    def __init__(self):
        self.age = 21
        self.hight = 160
    def print_info(self):
        print(f'my girlfriend age is {self.age}' )

someone1 = girlfriend()
# Here, we do not call the metheod init, but it has been called when we create the instance
someone1.print_info()

# use magic method to assign different value
class boyfriend():
    def __init__(self, age, hight):
        self.age = age
        self.hight = hight
    def print_info(self):
        print(f'my boyfriend age is {self.age}' )

someone2 = boyfriend(20, 180)
someone3 = boyfriend(24, 170)
someone3.print_info()

# lambda, simplify the code
# can accept any number of argument but output only one

# use function to print 100
def fn1():
    return 100

print(fn1())
print(fn1)

# use lambda to print 100
fn2 = lambda: 100
print(fn2)   # fn2 is where lambda stores
print(fn2())

# compare normal function and lambda
# compute a + b
def add(a, b):
    return a + b
print(add(1,2))

fn3 = lambda a, b:a+b
print(fn3(1,2))
