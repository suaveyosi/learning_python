def my_func(arg1,arg2,arg3=1,arg4=2):
    return ((arg1+arg2)/arg3)*arg4

print(my_func(2,3))
print(my_func(2,3,5,2))
print(my_func(2,3,arg4=2,arg3=5))