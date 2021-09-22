def outer(f): #2
    def inner(): #4
        result=f() #5
        return result ** 2 # 5**2
    return inner #3


@outer
def num():
    return 5


print(num())