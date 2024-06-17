#Demo function.py

def setValue(newValue):
    x=newValue
    print("지역변수:",x)

retValue = setValue(5)

print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))



#스코핑룰
x=5
def func(a):
    return a+x
print(func(1))

def func2(a):
    x=1
    return a+x
print(func2(1))
