def total(a,b):
    return a+b

# print(total(3,4,3,4))    

def all_total(*args):
    total=0
    for nums in args:
        total+=nums
    return total    


print(all_total(2,3,4))