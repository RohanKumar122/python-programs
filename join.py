lst=["john",'rohan','ramesh','hemant','jiya']
for item in lst:
    print(item,"and",end=" ")
print("\n")    

a=(" and ".join(lst)) 
print(a)
lst[4]="jai"
print(a)